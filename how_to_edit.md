1. Copy the contents from the chosen `.md` file into Visual Studio Code. Edit content as needed.
2. In Visual Studio Code, download the extension **Markdown PDF** by yzane.
3. Open the `.md` file, right click then select `Markdown PDF: Export (pdf)`.
<div style="text-align: center"><img src="https://i.imgur.com/YOUw7uq.png" width="50%"></div>

Tip: Use **[ShareX](https://getsharex.com/downloads)** to automate the upload workflow such that a region screen capture is "converted" into an imgur link.

How to setup ShareX:
1. From menu, open **ShareX**.
2. Under "Capture", ensure that the "Show cursor" is disabled. (Bold means the option is enabled.)
<img src="https://i.imgur.com/kpf2YQm.png">
4. Under "After capture task", enable "Upload image to host".
<img src="https://i.imgur.com/lIMgr6e.png">
5. Under "After upload task", enable "Copy URL to clipboard"
<img src="https://i.imgur.com/A80wakf.png">

Take the automated workflow a step further by automatically turning these links into tags with [AutoHotkey v2.0](https://www.autohotkey.com/)

1. From menu, open **AutoHotkey Dash**.
2. Click "New script".
3. In the field with placeholder Untitled, type:
```img-link-to-md```
<img src="https://i.imgur.com/vnpVmgT.png">
3. Click `Edit`.
4. Select Notepad as the editor.
5. Paste the following:

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
6. Save the file: `Ctrl + S`.
7. From the library, double-click the `img-link-to-md.ahk` to run the script.

(To stop the script, simply right-click the AutoHotkey Dash icon from the task bar then click "Exit".)

Now your workflow is as simple as:
1. Take a screenshot using `Ctrl + Fn + Prt Sc`.
2. Paste the formatted `Ctrl + Win + V` to paste the wrapped HTML code.