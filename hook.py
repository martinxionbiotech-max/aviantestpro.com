"""MkDocs post-build hook: create Cloudflare Pages _redirects file"""
import os

def on_post_build(config, **kwargs):
    site_dir = config['site_dir']
    redirects_path = os.path.join(site_dir, '_redirects')
    with open(redirects_path, 'w') as f:
        f.write('# Cloudflare Pages _redirects for MkDocs\n')
        f.write('/  /index.html  200\n')
        f.write('/*  /index.html  200\n')
    return config
