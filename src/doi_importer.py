
from config import app
import requests
import json

# FROM: https://gist.github.com/brews/8d3b3ede15d120a86a6bd6fc43859c5e
def fetchmeta(doi, fmt='dict', **kwargs):
    """Fetch metadata for a given DOI.
    Parameters
    ----------
    doi : str
    fmt : str, optional
        Desired metadata format. Can be 'dict' or 'bibtex'.
        Default is 'dict'.
    **kwargs :
        Additional keyword arguments are passed to `json.loads()` if `fmt`
        is 'dict' and you're a big JSON nerd.
    Returns
    -------
    out : str or dict or None
        `None` is returned if the server gives unhappy response. Usually 
        this means the DOI is bad.
    Examples
    --------
    >>> fetchmeta('10.1016/j.dendro.2018.02.005')
    >>> fetchmeta('10.1016/j.dendro.2018.02.005', 'bibtex')
    
    References
    ----------
    https://www.doi.org/hb.html
    """
    # Parse args and setup the server response we want.
    accept_type = 'application/'
    if fmt == 'dict':
        accept_type += 'citeproc+json'
    elif fmt == 'bibtex':
        accept_type += 'x-bibtex'
    else:
        raise ValueError("`fmt` must be 'dict' or 'bibtex'")

    # Request data from server.
    url = "https://dx.doi.org/" + str(doi)
    header = {'accept': accept_type}
    r = requests.get(url, headers=header)

    # Format metadata if server response is good.
    out = None
    if r.status_code == 200 and fmt == 'dict':
        out = json.loads(r.text, **kwargs)
    elif r.status_code == 200 and fmt == 'bibtex':
        out = r.text

    return out

def convert_doi(doi_link : str):
    if (len(doi_link) == 0 or doi_link.find('doi.org/') == -1):
        raise Exception("Invalid doi")

    doi = doi_link.split('doi.org/')[1]
    meta = fetchmeta(doi, fmt = 'bibtex')

    def is_type(type : str):
        return meta.startswith(f" @{type}{'{'}")

    def get_value(type : str):
        type += '={'
        s = meta.find(type) + len(type)
        return meta[s : meta.find('}', s, None)]

    if (is_type('article')):
        return ('article', { 'author': get_value('author'), 'title': get_value('title'), 'year': get_value('year'), 'journal': get_value('journal') })

    return None


if __name__ == "__main__":
    with app.app_context():
      print(convert_doi('https://doi.org/10.1145/3651278'))
      print('\n')
      print(convert_doi('https://doi.org/10.1145/3674735'))
