import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from pathlib import Path
from typing import Optional, List

import fiftyone as fo
from PIL import Image
from tqdm import tqdm


def voc2coco(data_dir: str, image_set: str, classes: Optional[List[str]] = None,
             export_dir: Optional[str] = None) -> None:
    """Converts VOC Dataset to COCO format.

    Args:
        data_dir (str): Root directory to VOC Dataset.
        image_set (str): Select the image_set to use.
        classes (list, optional): A list of possible class labels.
            If not provided, this list will be extracted from the dataset.
        export_dir (str, optional): Directory to write converted dataset.
    """
    data_dir = Path(data_dir).expanduser()
    img_dir = data_dir / "JPEGImages"
    image_set = data_dir / "ImageSets" / "Main" / f"{image_set}.txt"
    ann_dir = data_dir / "Annotations"
    dataset = fo.Dataset()

    with open(image_set) as fp:
        filenames = [f.strip() for f in fp.readlines()]
        ann_files = [ann_dir / f"{filename}.xml" for filename in filenames]

    for img_id, filepath in enumerate(tqdm(ann_files)):
        root = ET.parse(filepath).getroot()
        # filename = Path(root.findtext("filename"))
        filename = f"{filepath.stem}.jpg"
        filepath = img_dir / filename
        assert filepath.exists(), f"{filepath} not found."

        sample = fo.Sample(filepath)
        width, height = Image.open(filepath).size
        detections = []

        for _, obj in enumerate(root.findall("object")):
            name = obj.findtext("name")
            bbox = obj.find("bndbox")

            xmin = float(bbox.findtext("xmin")) / width
            ymin = float(bbox.findtext("ymin")) / height
            xmax = float(bbox.findtext("xmax")) / width
            ymax = float(bbox.findtext("ymax")) / height
            w = xmax - xmin
            h = ymax - ymin

            detections.append(fo.Detection(
                label=name, bounding_box=[xmin, ymin, w, h]
            ))

        sample["ground_truth"] = fo.Detections(detections=detections)
        dataset.add_sample(sample)

    labels_dir = Path(export_dir) if export_dir is not None else data_dir
    labels_path = labels_dir / f"{image_set.stem}.json"

    dataset.export(
        export_dir=export_dir,
        dataset_type=fo.types.COCODetectionDataset,
        label_field="ground_truth",
        labels_path=labels_path,
        classes=classes,
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--export_dir")
    parser.add_argument("--image_set", required=True)
    parser.add_argument("--classes", nargs="+",
                        help="A list of possible class labels.")
    args = parser.parse_args()
    voc2coco(args.data_dir, args.image_set, classes=args.classes)
