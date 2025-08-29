from enum import Enum

from ..config import DirectoryPaths

MPL_STYLE_DIR = DirectoryPaths.MPL_STYLE_DIR.value

class Styles(Enum):
    """Enum for Matplotlib styles used in the project."""

    CMR10 = MPL_STYLE_DIR / "iragca_cmr10.mplstyle"
    ML = MPL_STYLE_DIR / "iragca_ml.mplstyle"
    ML2 = MPL_STYLE_DIR / "iragca_ml2.mplstyle"
