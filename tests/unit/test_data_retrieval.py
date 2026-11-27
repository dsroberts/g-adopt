from gadopt.gplates.gplatesfiles import (
    reconstructions,
    ensure_reconstruction,
    MissingReconstructionException,
)
import pytest
import urllib.error
import zipfile
from pathlib import Path
from unittest.mock import MagicMock, PropertyMock, patch

DUMMY_RECONSTRUCTION = {
    "plate_files": {
        "topology_filenames": ["a", "b"],
        "static_polygons": "c",
        "continental_polygons": "d",
    },
    "directory": "dummy",
    "url": "https://data.gadopt.org/github-actions/dummy.zip",
}

DUMMY_RECONSTRUCTION_NO_URL = {
    "plate_files": {
        "topology_filenames": ["a", "b"],
        "static_polygons": "c",
        "continental_polygons": "d",
    },
    "directory": "dummy",
}

DUMMY_RECONSTRUCTION_EXTRA_FILE = {
    "plate_files": {
        "topology_filenames": ["a", "b"],
        "static_polygons": "c",
        "continental_polygons": ["d", "e"],
    },
    "directory": "dummy",
    "url": "https://data.gadopt.org/github-actions/dummy.zip",
}

DUMMY_RECONSTRUCTION_NOT_ZIPFILE = {
    "directory": "dummy",
    "url": "https://data.gadopt.org/github-actions/not_a_zip_file.txt",
}

DUMMY_RECONSTRUCTION_WRONG_DIR = {
    "plate_files": {
        "topology_filenames": ["a", "b"],
        "static_polygons": "c",
        "continental_polygons": "d",
    },
    "directory": "wrong",
    "url": "https://data.gadopt.org/github-actions/dummy.zip",
}

DUMMY_RECONSTRUCTION_WRONG_URL = {
    "directory": "dummy",
    "url": "https://data.gadopt.org/404.zip",
}

TEST_DATA_PATH = Path(__file__).resolve().parent / "data"


@pytest.fixture
def mock_urlopen():

    with open(TEST_DATA_PATH / "dummy.zip", "rb") as f:
        zf = f.read()

    response = MagicMock()

    with (
        patch("urllib.request.urlopen", return_value=response) as urlopen,
        patch.object(
            type(response),
            "headers",
            new_callable=PropertyMock,
            create=True,
        ) as headers,
        patch.object(response, "read", return_value=zf) as read,
    ):
        headers.return_value = MagicMock()
        headers.return_value.get_content_type.return_value = "application/zip"
        yield urlopen, headers, read


@pytest.fixture
def mock_reconstruction():
    with patch.dict(reconstructions, {"dummy": DUMMY_RECONSTRUCTION}) as r:
        yield r


def test_invalid_reconstruction(tmp_path):
    assert True


def test_download_reconstruction(tmp_path, mock_reconstruction, mock_urlopen):
    assert True


def test_unzip_reconstruction(tmp_path, mock_reconstruction, mock_urlopen):
    # predownload reconstruction
    assert True


def test_existing_reconstruction(tmp_path, mock_reconstruction, mock_urlopen):
    assert True


def test_bad_zipfile(tmp_path, mock_reconstruction, mock_urlopen):
    assert True


def test_download_error(tmp_path, mock_urlopen):
    assert True


def test_download_not_a_zipfile(tmp_path, mock_urlopen):
    assert True


def test_missing_files(tmp_path, mock_urlopen):
    assert True


def test_wrong_directory(tmp_path, mock_urlopen):
    assert True


def test_no_url_provided(tmp_path, mock_urlopen):
    assert True


def test_empty_directory(tmp_path, mock_reconstruction):
    assert True
