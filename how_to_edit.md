
# Guide for Editing and Exporting in VS Code Windows

## Table of Contents
- [How to edit a markdown file in VS Code](#how-to-edit-a-markdown-file-in-vs-code)
  - [How to speed up your workflow for adding images](#how-to-speed-up-your-workflow-for-adding-images)
  - [How to setup ShareX](#how-to-setup-sharex)
  - [How to setup AutoHotkey](#how-to-setup-autohotkey)
  - [How to speed up workflow for Find and Replace to add images](#how-to-speed-up-workflow-for-find-and-replace-to-add-images)
- [How to export a markdown file into PDF in VS Code](#how-to-export-a-markdown-file-into-pdf-in-vs-code)

## How to create a markdown file of a PDF of scanned images
1. In your preferred browser, open **[PaddleOCR](https://aistudio.baidu.com/paddleocr)**.
2. In the Select Model dropdown, choose **PaddleOCR-VL** (latest version available).
    <div style="text-align: center;">
        <img src="https://i.imgur.com/KzmiWi7.png" alt="Image" width="80%">
    </div>
3. Upload the PDF of scanned images. Wait for the model to finish parsing.
4. Click the **Download** button then select **Markdown**.
    <div style="text-align: center;">
        <img src="https://i.imgur.com/R5HWDzv.png" alt="Image" width="80%">
    </div>

## How to edit the PaddleOCR-generated markdown file in VS Code
1. In VS Code, install the extension **[Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)** by *yzane*.
2. In VS Code, create your own `.md` file.
3. From this GitHub repository, open the target `.md`then copy and paste it into the `.md` file created from Step 2.
4. Preview the markdown as you edit using VS Code's built-in preview: click the three dots (`...`) in the top-right corner of the editor and select **Reopen Editor With** > **Markdown Preview**.

   <div style="text-align: center;">
    <img src="https://i.imgur.com/2cCuB13.png" alt="Image">
   </p>

   (or use the shortcut `Ctrl + Shift + V`)

5. Edit content as needed, view the supported markdown syntax [here](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf).

### How to speed up your workflow for adding images
> [!NOTE]
> For the images to be accessible anywhere no matter the device, images in a markdown file should be links.

> [!TIP]
> Use **[ShareX](https://getsharex.com/downloads)** to instantly upload region screen captures and automatically copy an Imgur link to your clipboard.
 
#### How to setup ShareX:
1. From the Start Menu, open **ShareX**.
2. Under **Capture**, ensure **Show cursor** is disabled. *(Note: Bold means the option is enabled.)*

<p align="center"><img src="https://i.imgur.com/kpf2YQm.png" width="80%"></p>

3. Under **After capture task**, enable **Upload image to host**.

<p align="center"><img src="https://i.imgur.com/lIMgr6e.png" width="80%"></p>

4. Under **"After upload task"**, enable **Copy URL to clipboard**.

<p align="center"><img src="https://i.imgur.com/A80wakf.png" width="80%"></p>

> [!TIP]
> Take the automated workflow a step further by automatically turning these links into tags with **[AutoHotkey v2.0](https://www.autohotkey.com/)**

#### How to setup AutoHotkey:
1. From the Start Menu, open **AutoHotkey Dash**.
2. Click **New script**.
3. In the text field, name your script:
`img-link-to-md`.
   
   <p align="center"><img src="https://i.imgur.com/cVp1mek.png" width="34%"></p>

4. Click **Edit** and select **Notepad** as your editor.
5. In the opened Notepad editor (`img-link-to-md.ahk`), paste the following script:

    ```
    #Requires AutoHotkey v2.0

    ^#v:: {
        ; Grab clipboard and strip any accidental trailing spaces or newlines
        url := Trim(A_Clipboard, " `t`r`n")
        
        ; Check if it ends in an image extension or is hosted on a known image site
        isImageExt := RegExMatch(url, "\.(png|jpg|jpeg|gif|webp|svg)(\?.*)?$")
        isImageHost := RegExMatch(url, "i)(imgur\.com|cloudinary\.com|ibb\.co|gyazo\.com)")

        if (isImageExt || isImageHost) {
            wrappedHTML := '<div style="text-align: center;">`n    <img src="' . url . '" alt="Image" width="40%">`n</div>'
            A_Clipboard := wrappedHTML
            Send("^v")
        } else {
            Send("^v")
        }
    }
    ```
    This script is specific to **AutoHotkey v2.0**.

6. Save the file (`Ctrl + S`).
7. From the File Explorer (e.g., `C:\Users\GUEST USER\Documents\AutoHotkey`), double-click the `img-link-to-md.ahk` to run the script.

> [!NOTE]
> To stop the script later, simply right-click the green AutoHotkey Dash icon in your taskbar tray and click **Exit**.

Now your workflow is as simple as:
1. Take a screenshot: `Ctrl + Fn + Prt Sc`.
2. Paste the wrapped HTML code: `Ctrl + Win + V`.

> [!WARNING]
> If you move your cursor and press `Ctrl + Win + V` again on a link that is already wrapped or inside a block, it will nest the `<div>` inside another `<div>`. You may need to manually clean up nested wrappers if triggered multiple times in the same spot.

### How to speed up workflow in adding images to AVAILABLE PARTS section 
1. In the markdown file for the digitized version of the book (e.g., [Act_One.md](./Act_One.md)), focus on typing all the available parts in this format:

    ```
    #### AVAILABLE PARTS
    - 1 \times Capacitor (0.001 F)
    - 2 \times Chain
    - 3 \times Diode
    - 4 \times Inductor (55 H)
    - 5 \times Junction
    - 6 \times 200 Ohm
    - 7 \times 500 Ohm
    - 8 \times 1000 Ohm
    - 9 \times Switch
    - 10 \times Transistor
    ```

2. Once all **AVAILABLE PARTS** section have been typed in, open the Find and Replace widget (`Ctrl + H`).
3. Click the Regex icon (`.*`) beside the Find input field to enable regular expressions.
4. Enter the Find and Replace expressions in the input fields, respectively.

> [!TIP]
> You may refer to **[this cheatsheet](./available_parts_cheatsheet.md)** for a pre-made list of find and replace values for each available part.

For example:
To find all instances of `\times Junction` not followed by a `<div` and replace that with

× Junction
    <div style="text-align: left;">
        <img src="https://i.imgur.com/5UAaJ3l.png" alt="Image" width="8%">  
    </div>
Fill the Find and Replace fields with the following:
- Find:
    ```
    (\\times Junction)\r?\n(?!\s*<div)
    ```
    - Explanation:
        - `\r?\n` targets the line break immediately following the `- 1 \times Junction` text
        - `(?!\s*<div)`
            - `?!` look ahead and ensure that the find matches are not followed by
            - `\s*` any whitespace characters (e.g., spaces, tabs) and a
            - `<div` tag
- Replace:
    ```
    × Junction\n    <div style="text-align: left;">\n        <img src="https://i.imgur.com/5UAaJ3l.png" alt="Image" width="8%">\n    </div>
    ```

> [!TIP]
> You may refer to [this cheatsheet](./available_parts_cheatsheet.md) for a pre-made list of find and replace values for each available part.

## How to export a markdown file into PDF in VS Code
1. Open the `.md` file, right-click anywhere in the editor, and select `Markdown PDF: Export (pdf)`.
<p align="center"><img src="https://i.imgur.com/YOUw7uq.png" width="34%"></p>
