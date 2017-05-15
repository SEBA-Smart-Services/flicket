#! usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template

def display_post_box(ticket=None, post=None, replies=None, loop=None, page=None):
    """
    :param ticket: object containing ticket information
    :param post: 
    :param replies:
    :param loop: 
    :param page: 
    :return: 
    """

    if post is None:
        content = ticket
        post_id = None
        ticket_rid = ticket.id
    else:
        content = post
        post_id = post.id
        ticket_rid = None

    return render_template('flicket_post.html', ticket=ticket, post=post, content=content, replies=replies, loop=loop, page=page, post_id=post_id, ticket_rid=ticket_rid)
