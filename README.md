# PicoDuckySnippet
![Hackatime project time spent](https://hackatime-badge.hackclub.com/U0968G9HWS1/PicoDuckySnippet)

## What is this?
PicoDuckySnippet is code designed to be ran on the [PicoDucky](https://github.com/Outdatedcandy92/PicoDucky), a USB Rubber Ducky style device based on the Raspberry Pi Pico. The code allows the PicoDucky to write out various user-defined snippets stored in the `snippets.json` file, writing specific ones based on the morse code they use.

## Preview
![Demo of PicoDuckySnippet in action](PicoDuckySnippetDemo.gif)
> I only realised after recording this that the footage was low resolution, sorry about that!

## How to Install
1. **Setup the PicoDucky**: Follow the instructions on the [PicoDucky GitHub page](https://github.com/Outdatedcandy92/PicoDucky#as-a-hid-device) to set up your PicoDucky as a HID Device.
2. **Add the code**: Replace the `code.py` file in the CIRCUITPY drive with the one in this repository.
3. **Add the snippets file**: Add the `snippets.json` file to the CIRCUITPY drive. This file contains the snippets that the PicoDucky will type out.
4. **Edit snippets**: Open the `snippets.json` file and add your desired snippets in JSON object format. For example:
   ```json
   {
       ".-": "Snippet 1",
       "-...": "Snippet 2",
       "-.-.": "Snippet 3"
   }
   ```

## How to use
1. **Connect the PicoDucky**: Plug the PicoDucky into a USB port on your computer.
2. **Typing a snippet**: Use Morse code on the button labelled "button" to input the snippet you want to type. For example, to type "Snippet 1", you would input the Morse code for ".-". 

## Why I made this
I made this as part of the Hack Club PicoDucky YSWS event. I wanted a simple way to manage and use text snippets that would work on pretty much any device with a USB port and that would be easy to set up and use, and this code provides that functionality. You can learn more about the event [here](https://picoducky.hackclub.com/).