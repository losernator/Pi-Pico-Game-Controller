import usb_hid
import usb_midi
import storage
import board
import digitalio

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x05,  #   Report ID (5)
    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x10,  #   Usage Maximum (Button 16)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x10,  #   Report Count (16)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x00,  #   Logical Minimum (0)
    0x26, 0xFE, 0x00, #   Logical Maximum (254)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x09, 0x39,  #   USAGE (Hat switch)
    0x15, 0x01,  #   LOGICAL_MINIMUM (1)
    0x25, 0x08,  #   LOGICAL_MAXIMUM (8)
    0x35, 0x00,  #   PHYSICAL_MINIMUM (0)
    0x46, 0x3B, 0x01,  #    PHYSICAL_MAXIMUM(315)
    0x66, 0x14, 0x00, #   UNIT (Eng Rot:Angular Pos)
    0x75, 0x04,  #   REPORT_SIZE (4)
    0x95, 0x01,  #   REPORT_COUNT (1)
    0x81, 0x42,  #   INPUT (Data,Var,Abs)
    0x75, 0x04,  #   Report Size (4)
    0x95, 0x01,  #   Report Count (1)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x00,  #   Logical Maximum (0)
    0x35, 0x00,  #   Physical Minimum (0)
    0x45, 0x00,  #   Physical Maximum (0)
    0x65, 0x00,  #   Unit (None)
    0x81, 0x03,  #   Input (Const,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,        # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(5,),           # Descriptor uses report ID 5.
    in_report_lengths=(7,),    # This gamepad sends 7 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable((gamepad,))
usb_midi.disable()

button = digitalio.DigitalInOut(board.GP2)
button.switch_to_input(pull=digitalio.Pull.UP)

if not button.value:
    storage.disable_usb_drive()    # Hide drive
    usb_cdc.disable()              # REPL off
'''
if not button.value:
    storage.remount("/", False)
'''
