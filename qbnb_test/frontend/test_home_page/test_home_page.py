from pathlib import Path
import subprocess


def test_home_page():
    """
    Covers basic tests surrounding the user home page
    """
    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_home_page.in'))
    expected_out = open(current_folder.joinpath(
        'test_home_page.out'), newline='\r\n').read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    # make assertion for in/out
    print('outputs', output)
    assert output.strip() == expected_out.strip()
