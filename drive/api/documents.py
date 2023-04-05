import frappe
import uuid
from drive.utils.files import get_user_directory, create_user_directory


@frappe.whitelist()
def create_document(title, content, parent=None):
    try:
        user_directory = get_user_directory()
    except FileNotFoundError:
        user_directory = create_user_directory()
    parent = frappe.form_dict.parent or user_directory.name
    drive_document = frappe.get_doc({
        'doctype': 'Drive Document',
        'name': uuid.uuid4().hex,
        'title': title,
        'content': content,
        'parent_drive_entity': parent,
    })
    drive_document.insert()

@frappe.whitelist()
def get_documents_in_path(parent_drive_entity):
    """
    Returns all tags of parent entity

    :param entity: Entity name
    """

    return frappe.db.get_list('Drive Document',
                              filters={
                                'parent_drive_entity': parent_drive_entity,
                                'owner': frappe.session.user
                              },
                              fields=['name', 'title', 'content'],
                              )
