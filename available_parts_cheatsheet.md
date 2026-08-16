# Find and Replace Cheatsheet for Available Parts

## Capacitor
Find:	
```
(\\times Capacitor \(0.001 F\))\r?\n(?!\s*<div)
```

Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/ywxLN0P.png" alt="Image" width="8%">\n	</div>\n
```

## Chain
Find:
```
(\\times Chain)\r?\n(?!\s*<div)
```
Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/0X4m4YM.png" alt="Image" width="8%">\n	</div>\n
```

## Diode
```
Find:
(\\times Diode)\r?\n(?!\s*<div)
```
Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/8Kv9XsS.png" alt="Image" width="8%">\n	</div>\n
```

## Inductor
Find:
```
(\\times Inductor \(55 H\))\r?\n(?!\s*<div)
```
Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/Rg4WZvk.png" alt="Image" width="8%">\n	</div>\n
```

## Junction
Find:
```
(\\times Junction)\r?\n(?!\s*<div)
```
Replace:
```
$1\n    <div style="text-align: left;">\n        <img src="https://i.imgur.com/5UAaJ3l.png" alt="Image" width="8%">\n    </div>\n
```

## Resistor

### 200 Ohm
Find:
```
(\\times 200 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/bip0kxG.png" alt="Image" width="8%">\n	</div>\n
```
### 500 Ohm
Find:
```
(\\times 500 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
$1\n<div style="text-align: left;">\n		<img src="https://i.imgur.com/MAay07O.png" alt="Image" width="8%">\n	</div>\n
```

### 1000 Ohm
Find:
```
(\\times 1000 Ohm)\r?\n(?!\s*<div)
```
Replace:
```
$1\n<div style="text-align: left;">\n		<img src="https://i.imgur.com/VuQ2evV.png" alt="Image" width="8%">\n	</div>\n
```

## Switch
Find:
```
(\\times Switch)\r?\n(?!\s*<div)
```
Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/HDJweSl.png" alt="Image" width="8%">\n	</div>\n
```

## Transistor
Find:
```
(\\times Transistor)\r?\n(?!\s*<div)
```

Replace:
```
$1\n	<div style="text-align: left;">\n	<img src="https://i.imgur.com/X4Au9IK.png" alt="Image" width="8%">\n	</div>\n
```