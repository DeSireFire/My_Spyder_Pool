from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from PIL import Image
import os

input = getattr(__builtins__, 'raw_input', input)

def main():
    # redirect_uri = "http://localhost:8080/"
    redirect_uri = "https://github.com/DeSireFire/AlienVan/"
    client_secret = "vpSUH80#^xtdwvWCSI194*|"
    # client_secret = "BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM"

    client = onedrivesdk.get_default_client(client_id='e2d585cd-751f-4c7e-aab7-d8b48c485f94',
    # client = onedrivesdk.get_default_client(client_id='00000000481695BB',
                                            scopes=['wl.signin',
                                                    'wl.offline_access',
                                                    'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # 阻止线程，直到我们有code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    # 最后，验证!
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    item_id = "root"
    copy_item_ids = None
    action = 0

    while True:
        items = navigate(client, item_id)
        print("0: UP")
        count = 0
        for count, item in enumerate(items):
            print("{} {}".format(count+1, item.name if item.folder is None else "/"+item.name))

        selected = input("选择项目，输入'C'复制全部，输入'L'列出当前文件夹中的更改: ")

        if selected == "C":
            copy_item_ids = []
            for item in items:
                copy_item_ids.append(item.id)

        elif selected == "L":
            token = input("输入您的令牌，如果没有，则输入任何内容: ")
            list_changes(client, item_id, token)

        else:
            selected = int(selected)

            if selected == 0:
                item_id = get_parent_id(client, item_id)
            else:
                action = int(input("选择操作：1：导航 2：重命名 3：查看缩略图 4：获取共享链接 5：列表更改 6：下载 7：上载 8：删除 9：复制{} ... ".format(" 10: 粘贴" if copy_item_ids else "")))
                if items[selected-1].folder is None or (action != 6 and action != 1):
                    if action == 1:
                        print("无法导航文件")
                    elif action == 2:
                        rename(client, items[selected-1].id)
                    elif action == 3:
                        view_thumbnail(client, items[selected-1].id)
                    elif action == 4:
                        get_sharing_link(client, items[selected-1].id)
                    elif action == 5:
                        token = input("输入您的令牌，如果没有，则输入任何内容: ")
                        list_changes(client, items[selected-1].id, token)
                    elif action == 6:
                        download(client, items[selected-1].id)
                    elif action == 7:
                        if item.folder is None:
                            print("您无法上传到文件")
                        else:
                            upload(client, items[selected-1].id)
                    elif action == 8:
                        delete(client, items[selected-1].id)
                    elif action == 9:
                        copy_item_ids = [items[selected-1].id]
                    elif action == 10 and copy_item_ids:
                        if items[selected-1].folder:
                            paste(client, items[selected-1].id, copy_item_ids)
                        else:
                            print("无法复制到文件")
                else:
                    item_id = items[selected-1].id


def navigate(client, item_id):
    items = client.item(id=item_id).children.get()
    return items


def rename(client, item_id):
    new_name = input("Enter new name: ")
    renamed_item = onedrivesdk.Item()
    renamed_item.name = new_name
    renamed_item.id = item_id
    client.item(id=item_id).update(renamed_item)


def view_thumbnail(client, item_id):
    if len(client.item(id=item_id).thumbnails.get()) == 0:
        print("File does not have any thumbnails!\n")
    else:
        action = int(input("Size? 1:Small 2:Medium 3:Large... "))
        try:
            os.remove("./tmp_thumb.jpg")
        except:
            pass
        if action == 1:
            client.item(id=item_id).thumbnails[0].small.download("./tmp_thumb.jpg")
        elif action == 2:
            client.item(id=item_id).thumbnails[0].medium.download("./tmp_thumb.jpg")
        elif action == 3:
            client.item(id=item_id).thumbnails[0].large.download("./tmp_thumb.jpg")
        image = Image.open("./tmp_thumb.jpg")
        image.show()


def get_sharing_link(client, item_id):
    action = int(input("Type? 1:View 2:Edit... "))
    permission = client.item(id=item_id).create_link("view" if action == 1 else "edit").post()
    print("\n{}\n".format(permission.link.web_url))


def download(client, item_id):
    directory = input("Enter download directory (can be relative): ")
    client.item(id=item_id).download(directory)


def upload(client, item_id):
    directory = input("Enter upload file directory (can be relative): ")
    name = input("Enter file name with extension: ")
    client.item(id=item_id).children[name].upload(directory)


def delete(client, item_id):
    confirm = input("Confirm delete? Y/N: ")
    if confirm == "Y":
        client.item(id=item_id).delete()


def paste(client, item_id, copy_item_ids):
    ref = onedrivesdk.ItemReference()
    ref.id = item_id
    for id in copy_item_ids:
        client.item(id=id).copy(parent_reference=ref).post()


def list_changes(client, item_id, token):
    collection_page = client.item(id=item_id).delta(token).get()
    for item in collection_page:
        print(item.name)

    print("TOKEN: {}".format(collection_page.token))


def get_parent_id(client, item_id):
    id = client.item(id=item_id).get().parent_reference.id
    return id

if __name__ == "__main__":
    main()