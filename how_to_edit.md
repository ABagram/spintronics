## How to edit and export markdown files
1. Copy the contents from your target `.md` file into **Visual Studio Code** and edit content as needed.
2. View markdown syntax supported [here](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf).

## How to export markdown files
1. In VS Code, download the extension **[Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)** by *yzane*.
2. Open the `.md` file, right-click anywhere in the editor, and select `Markdown PDF: Export (pdf)`.
<div style="text-align: center"><img src="https://i.imgur.com/YOUw7uq.png" width="50%"></div>

### How to speed up your workflow for adding/changing images
> [!NOTE]
> For the images to be accessible anywhere no matter the device, images in a markdown file should be links.

> [!TIP]
> Use **[ShareX](https://getsharex.com/downloads)** to instantly upload region screen captures and automatically copy an Imgur link to your clipboard.
 
#### How to setup ShareX:
1. From the Start Menu, open **ShareX**.
2. Under **Capture**, ensure **Show cursor** is disabled. *(Note: Bold means the option is enabled.)*
<img src="https://i.imgur.com/kpf2YQm.png">
3. Under **After capture task**, enable **Upload image to host**.
<img src="https://i.imgur.com/lIMgr6e.png">
4. Under **"After upload task"**, enable **Copy URL to clipboard**.
<img src="https://i.imgur.com/A80wakf.png">

> [!TIP]
> Take the automated workflow a step further by automatically turning these links into tags with **[AutoHotkey v2.0](https://www.autohotkey.com/)**

1. From the Start Menu, open **AutoHotkey Dash**.
2. Click **New script**.
3. In the text field, name your script:
```img-link-to-md```.
<img src="https://i.imgur.com/vnpVmgT.png">
4. Click **Edit** and select **Notepad** as your editor.
5. Paste the following script:

```
#Requires AutoHotkey v2.0

^#v:: {
    ; Grab clipboard and strip any accidental trailing spaces or newlines
    url := Trim(A_Clipboard, " `t`r`n")
    
    ; Check if it ends in an image extension or is hosted on a known image site
    isImageExt := RegExMatch(url, "\.(png|jpg|jpeg|gif|webp|svg)(\?.*)?$")
    isImageHost := RegExMatch(url, "i)(imgur\.com|cloudinary\.com|ibb\.co|gyazo\.com)")

    if (isImageExt || isImageHost) {
        wrappedHTML := '<div style="text-align: center;">`n    <img src="' . url . '" alt="Image">`n</div>'
        A_Clipboard := wrappedHTML
        Send("^v")
    } else {
        Send("^v")
    }
}
```
6. Save the file (`Ctrl + S`).
7. From the File Explorer, double-click the `img-link-to-md.ahk` to run the script.

> [!IMPORTANT]
> To stop the script later, simply right-click the green AutoHotkey Dash icon in your taskbar tray and click **Exit**.)

Now your workflow is as simple as:
1. Take a screenshot: `Ctrl + Fn + Prt Sc`.
2. Paste the wrapped HTML code: `Ctrl + Win + V`.