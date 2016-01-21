# vgmparse
A Python module for parsing [VGM (Video Game Music)](https://en.wikipedia.org/wiki/VGM_(file_format))
files. `.vgm` and `.vgz` (Gzip compressed) files are supported.

Currently, only version 1.50 of the VGM specification is supported.

## Installation
The `vgmparse` module can be installed directly from GitHub using `pip`:

```
sudo pip install -e git+https://github.com/cdodd/vgmparse.git#egg=vgmparse
```

## Usage
First import the `vgmparse` module:

```
@>>> import vgmparse
```

### Opening a VGM File
Open a file in binary mode and pass the data to the `Parser` class:

```
@>>> file_data = open('go_straight.vgm', 'rb').read()
@>>> vgm_data = vgmparse.Parser(file_data)
```

### Read VGM Metadata
The VGM metadata is available as a `dict` in the `metadata` variable:

```
@>>> vgm_data.metadata
{'total_samples': 4609970, 'vgm_data_offset': 12, 'vgm_ident': b'Vgm ', 'gd3_offset': 1110192, 'version': 336, 'ym2151_clock': 0, 'eof_offset': 1110478, 'sn76489_clock': 3579545, 'ym2413_clock': 0, 'loop_samples': 3951361, 'sn76489_feedback': 9, 'ym2612_clock': 7670453, 'loop_offset': 50883, 'rate': 60, 'sn76489_shift_register_width': 16}
```

### GD3 Data
GD3 data (track title, artist, etc) is available as a `dict` in the `gd3_data`
variable:

```
@>>> vgm_data.gd3_data.keys()
dict_keys(['title_eng', 'console_jap', 'notes', 'game_eng', 'game_jap', 'artist_eng', 'vgm_creator', 'console_eng', 'artist_jap', 'title_jap', 'date'])

@>>> print(vgm_data.gd3_data['title_eng'].decode())
Go Straight

@>>> print(vgm_data.gd3_data['artist_eng'].decode())
Yuzo Koshiro
```

As per the [GD3 specification](http://www.smspower.org/uploads/Music/gd3spec100.txt?sid=03f36df3451132209c81c18cd231534f)
the GD3 data uses 2-byte character encoding, however the exact encoding is not
specified, leaving it up to the creator of the VGM file. This modules does not
attempt to interpret the encoding, leaving the raw 2-byte encoding intact from
the VGM file.

### VGM Commands
The VGM commands are available as a `list` of `dict`s in the variable
`command_list`:

```
@>>> vgm_data.command_list[:3]
[{'command': b'R', 'data': b'(\x00'}, {'command': b'R', 'data': b'(\x04'}, {'command': b'R', 'data': b'(\x01'}]
```

If a command does not have have any data then `data` will be `None`.

**Note:** `command_list` will not include any data block commands as the data
block is parsed out for you.

### Data Block
If a data block is present it is read into the `StringIO` variable
`data_block`. You can then seek within this as if it were a file:

```
@>>> vgm_data.data_block.seek(0)
0
@>>> vgm_data.data_block.read(5)
b'\x82\x88\x8a\x8a\x88'
```
