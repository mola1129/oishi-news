import numpy as np
old_urls = np.loadtxt('urls.txt', dtype='unicode')


def get_diff_urls(new_urls):
    new_urls = np.array(new_urls)
    diff = []
    for new in new_urls:
        if not (new in old_urls):
            diff.append(new)
    return diff


def save_urls(filename, urls):
    urls = np.array(urls)
    np.savetxt(filename, urls, fmt="%s")
