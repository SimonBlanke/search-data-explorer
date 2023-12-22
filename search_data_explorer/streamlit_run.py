# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import sys

from tde_streamlit import app


def main():
    path = sys.argv[1]
    plots = sys.argv[2:]
    app(path, plots)


if __name__ == "__main__":
    main()
