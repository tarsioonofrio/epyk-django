import os
import sys

from app.utils import refresh


def main():
    """
    This will transpile all the reports in the reports folder
    """
    template_path = os.path.join('app', 'reports')
    sys.path.append(template_path)
    for report in os.listdir(template_path):
        if report.endswith(".py"):
            view_name = report[:-3]
            refresh(view_name)


if __name__ == '__main__':
    main()
