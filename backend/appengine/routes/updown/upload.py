# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from blob_app import blob_facade
from gaepermission.decorator import login_not_required
from routes import updown
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
def index(_handler, files):
    blob_infos = _handler.get_uploads('files[]')
    cmd = blob_facade.save_blob_files_cmd(blob_infos)
    cmd.execute()
    path = router.to_path(updown)
    return RedirectResponse(path)