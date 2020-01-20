import numpy as np
import cloudinary.uploader


def get_diff_urls(new_urls, filename):
    new_urls = np.array(new_urls)
    old_urls = np.loadtxt(filename, dtype='unicode')
    diff = []
    for new in new_urls:
        if not (new in old_urls):
            diff.append(new)
    return diff


def save_urls(filename, urls):
    urls = np.array(urls)
    np.savetxt(filename, urls, fmt="%s")
    cloudinary.uploader.upload(
        file=filename, folder="oishi-news/", use_filename=True, unique_filename=False, resource_type="raw")
