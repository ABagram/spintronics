# Find and Replace Cheatsheet for Available Parts

The **AVAILABLE PARTS** across all challenges differ in combination, so while the name-image pair for each part is the same, having to type or paste the formatted wrapped HTML code every time would be tedious/repetitive.

Recommended workflow: 
1. Type down ALL PARTS under the **AVAILABLE PARTS** section across ALL CHALLENGES in this format:

    ```
    #### AVAILABLE PARTS
    - 1 \times Ammeter
    - 2 \times Capacitor (0.001 F)
    - 3 \times Chain
    - 4 \times Diode
    - 5 \times Inductor (55 H)
    - 6 \times Junction
    - 7 \times 200 Ohm
    - 8 \times 500 Ohm
    - 9 \times 1000 Ohm
    - 10 \times Switch
    - 11 \times Transistor
    ```

2. Once done, use the Find and Replace tool with Use Regular Expression (`.*`) enabled (`Alt + R`) then copy paste the values to the respective fields:

List of Available Parts
- [Ammeter](#ammeter)
- [Capacitor (0.001 F)](#capacitor-0001-f)
- [Chain](#chain)
- [Diode](#diode)
- [Inductor (55 H)](#inductor-55-h)
- [Junction](#junction)
- [Resistor](#resistor)
    - [200 Ω](#200-ohm)
    - [500 Ω](#500-ohm)
    - [1000 Ω](#1000-ohm)
- [Switch](#switch)
- [Transistor](#transistor)

## Ammeter

Find:
```
(\\times Ammeter)\r?\n(?!\s*<div)
```
Replace:
```
× Ammeter\n     <div style="text-align: left;">\n    <img src="https://i.imgur.com/c2cGliy.png" alt="Image" width="8%">\n   </div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Ammeter</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Ammeter<br>
          <img src="https://i.imgur.com/c2cGliy.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Capacitor (0.001 F)
Find:
```
(\\times Capacitor \(0.001 F\))\r?\n(?!\s*<div)
```

Replace:
```
× Capacitor (0.001 F)\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/ywxLN0P.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Capacitor (0.001 F)</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Capacitor (0.001 F)<br>
          <img src="https://i.imgur.com/ywxLN0P.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Chain
Find:
```
(\\times Chain)\r?\n(?!\s*<div)
```
Replace:
```
× Chain\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/0X4m4YM.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Chain</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Chain<br>
          <img src="https://i.imgur.com/0X4m4YM.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Diode
```
Find:
(\\times Diode)\r?\n(?!\s*<div)
```
Replace:
```
× Diode\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/8Kv9XsS.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Diode</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Diode<br>
          <img src="https://i.imgur.com/8Kv9XsS.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Inductor (55 H)
Find:
```
(\\times Inductor \(55 H\))\r?\n(?!\s*<div)
```
Replace:
```
× Inductor (55 H)\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/Rg4WZvk.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Inductor (55 H)</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Inductor (55 H)<br>
          <img src="https://i.imgur.com/Rg4WZvk.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Junction
Find:
```
(\\times Junction)\r?\n(?!\s*<div)
```
Replace:
```
× Junction\n    <div style="text-align: left;">\n        <img src="https://i.imgur.com/5UAaJ3l.png" alt="Image" width="8%">\n    </div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Junction</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Junction<br>
          <img src="https://i.imgur.com/5UAaJ3l.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Resistor

### 200 Ohm
Find:
```
(\\times 200 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
× 200 Ω\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/bip0kxG.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times 200 Ohm</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × 200 Ω<br>
          <img src="https://i.imgur.com/bip0kxG.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

### 500 Ohm
Find:
```
(\\times 500 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
× 500 Ω\n<div style="text-align: left;">\n		<img src="https://i.imgur.com/MAay07O.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times 500 Ohm</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × 500 Ω<br>
          <img src="https://i.imgur.com/MAay07O.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

### 1000 Ohm
Find:
```
(\\times 1000 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
× 1000 Ω\n<div style="text-align: left;">\n		<img src="https://i.imgur.com/VuQ2evV.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times 1000 Ohm</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × 1000 Ω<br>
          <img src="https://i.imgur.com/VuQ2evV.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Switch
Find:
```
(\\times Switch)\r?\n(?!\s*<div)
```
Replace:
```
× Switch\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/HDJweSl.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Switch</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Switch<br>
          <img src="https://i.imgur.com/HDJweSl.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Transistor
Find:
```
(\\times Transistor)\r?\n(?!\s*<div)
```

Replace:
```
× Transistor\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/X4Au9IK.png" alt="Image" width="8%">\n	</div>\n
```
Preview:
<div align="center">
  <table style="border: none; border-collapse: collapse; background: transparent;">
    <thead>
      <tr style="border: none; background: transparent;">
        <th style="border: none; text-align: left;">Find:</th>
        <th style="border: none;"></th>
        <th style="border: none; text-align: left;">Replace:</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border: none; background: transparent;">
        <td style="border: none; vertical-align: middle;">\times Transistor</td>
        <td style="border: none; vertical-align: middle; padding: 0 15px;">→</td>
        <td style="border: none; vertical-align: middle;">
          × Transistor<br>
          <img src="https://i.imgur.com/X4Au9IK.png" alt="Image" width="8%">
        </td>
      </tr>
    </tbody>
  </table>
</div>

> [!TIP]
> **Need to add a new part?**
> Use this template structure:
> **Find:**
> ```
> (\\times PartName)\r?\n(?!\s*<div)
> ```
> **Replace:**
> ```
> × PartName\n    <div style="text-align: left;">\n        <img src="YOUR_IMAGE_LINK" alt="Image" width="8%"><br>\n    </div>\n
> ```