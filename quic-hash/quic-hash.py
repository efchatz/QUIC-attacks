#MIT License
#Copyright (c) 2022 efchatz
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from scapy.all import *

for i in range(0,10):
    send(IP(dst="Server IP")/UDP(dport=443)/Raw(load='"\x00"')) 
    send(IP(dst="Server IP")/UDP(dport=443)/Raw(load='"\xc3\x00\x00\x00\x01\x08\x87\x0b\xc3\xb4\x98\x05\x79\x69\x08\x54\x4c\x28\x4e\x7c\x54\x2a\x3d\x00\x44\xe6\x52\x3b\x7e\x2e\x8b\xd2\x93\xf4\x0a\x65\x10\x86\xaf\x12\x97\xc4\x3a\xbd\x16\x53\x1b\x6d\x0c\xd8\x82\xf6\x70\xff\x30\xb6\x9e\x50\xb9\x9e\x6d\xc5\xf3\x7e\x44\xeb\x9a\x10\x12\xd0\x88\xe8\x76\x60\x36\xdc\x2b\x66\x77\xa0\x83\x4e\x52\xab\x83\x0f\x91\xc6\x38\xa4\xec\xf2\xe4\x37\x93\x6f\x9a\xe1\x0f\xc0\x7b\x15\x29\x71\xb3\x3f\xf4\x40\xd6\x6a\xbf\x17\x71\xb7\xcf\x51\xd2\xa6\xef\x8e\x3a\xd8\x0c\xcb\xbb\x50\xc2\xff\x8e\xd4\xaa\x83\xe8\x9c\xef\xd5\x41\xf6\x74\x97\xad\x42\x96\x1c\x42\xa9\xcb\x39\xd6\x9c\xcf\x1a\xa2\x40\xf9\xc3\x72\x27\x49\x9d\xc6\x59\xcf\x51\x34\x11\xa3\x44\x6a\xc6\xb8\x3d\x2d\xda\xbd\x6c\xf1\xb1\xd6\xda\xfd\x09\x03\x4f\xab\x1d\xe4\xa8\x93\x2d\x5f\x36\xcf\x47\x6d\xc6\xa4\x38\x0b\x52\x91\xf4\xb7\x8c\x92\xe4\xf0\xec\xa0\xc2\x89\xba\x1a\xc6\xbf\x21\x28\x21\xea\x6e\x70\xa7\xec\xde\x1a\x29\xf6\x08\xdb\xba\xc1\x3a\xfe\x70\x19\xe3\x13\xb3\x88\x64\xd5\x27\xd2\x84\x88\x71\x28\x79\x84\x33\x06\x70\xed\xfc\x64\xfb\xf1\xed\xac\x98\xdf\x77\x88\x38\x33\xaa\x00\x04\x73\x35\xed\x6e\x08\xaf\x37\x0c\x2f\x33\xb9\xb2\x5b\x5c\x8d\xd4\x05\x3d\xed\x89\x2f\x27\x93\xf4\x0e\x33\x7d\xb7\xc1\x6a\xc5\xa6\x6c\xd5\x4b\x21\x46\xcb\x5b\x5a\xbf\xd7\xd6\xbe\xff\x3b\xc6\x43\x19\x13\x9b\xe3\x1d\xef\xdd\xbf\xfe\x38\x29\x24\xe0\xea\xcc\xdd\xda\xa6\x00\x7e\x6b\x9d\x55\x1f\xc5\x16\x47\x92\xb3\x3c\xd8\x8a\x10\xd7\xd7\x04\x4c\x5c\x79\xa0\x4b\x10\x8e\x92\xec\x31\xe1\x0a\xc9\x4a\xd1\x0e\x49\xd7\xab\xdb\x34\xd0\x6d\x89\x9b\x49\xd5\xe1\x7b\xe8\xe7\x6d\x2d\x0e\xf7\xe7\x49\xd6\x94\xfd\xbe\x9d\xf8\x92\x0c\x23\x31\x2d\x0c\x8d\x6c\x0f\x36\xab\x7a\x4b\xbe\x19\x44\xb5\x38\x16\x6f\x9d\xf3\x2b\x82\x0e\x58\x84\x5f\xae\x2b\x69\x7c\xb1\x5b\x01\xa6\x61\x14\x0e\xf6\xd0\x89\x89\x57\xf4\x37\xde\x10\x72\x0f\xab\x30\x25\xbf\xd3\xc5\x9b\xae\xb2\x0e\x20\x12\xa8\x73\x2d\xb6\xd7\x56\x5b\x94\x8c\x66\x00\x3c\x80\xf8\x15\x24\x65\x59\xc4\x1d\xd9\x8f\x2d\x13\xb7\x3f\xa8\xc2\x14\x54\xc7\x49\xb0\x08\x92\x4d\x95\xd2\x2d\xf3\x89\x14\xd3\x86\x1d\x1a\x1f\xea\x8e\x9d\x23\xef\x06\x92\x16\x23\xd1\x0a\x9e\x24\x7e\xfc\x60\x7b\xac\x3e\x8c\x3d\xcc\xbd\x83\x8e\x95\x35\xcb\xaf\x00\x13\xb5\x9b\xfc\x6c\xb0\x58\x24\xac\xef\x17\xff\xfb\x93\xad\xfe\xcd\x01\xc5\x0a\xad\xa1\x03\x20\x23\xc4\x9b\xb4\x04\xc2\x2a\xe7\x4b\x2b\x1f\x0a\xd6\xa5\xf1\x36\x63\x27\xae\x70\xe1\xe9\xf5\x3d\x9f\x5b\x3a\x77\x0d\x6c\x98\x04\x86\xd6\x6b\xe7\xba\x64\x32\x22\x3d\x5f\x52\x2c\x9b\x5e\x08\x91\x20\xdc\x57\xf7\x6c\x9d\xef\x97\x1b\xf1\xf0\xa9\xf7\x20\xc7\xb5\xba\x0c\x0f\xc4\xda\x23\x3f\xaf\x9e\x77\xee\xfc\x49\x12\xee\xe9\x1c\x0f\x8d\x1d\x62\xff\xeb\x0f\xf5\x9b\x72\xdc\xa7\x93\x1c\xba\xa7\x95\x4d\x4c\xc7\x6a\xae\x69\x5e\xba\x37\xb0\xb3\xea\x6a\x71\x07\x77\xb8\x39\x0d\x01\xb8\x02\xeb\x30\x3b\xf5\x46\x95\xcb\xfa\x3b\x2a\x8d\x5d\x8b\xe4\xab\x46\x91\x16\xbb\xa4\xbc\x90\x08\x24\xaa\x48\x67\xe8\x4e\x2a\xdf\xa3\xae\xc1\xd0\x7f\xac\x86\x2e\x92\xb3\x23\xc0\x39\xd3\xa1\x60\xfc\x02\x95\x05\xc3\x06\x8f\x5e\xc7\x67\xe1\xa3\x58\x46\x43\xf3\x4d\xb3\x95\xf9\xa8\x94\x69\xc0\xa2\x02\x6b\x39\x1d\xa7\xe6\xe0\xc6\x4c\x3f\x1c\x0d\xde\x89\x33\x57\x65\x5e\xbf\xe8\xae\x58\x7f\xfe\x41\x06\x16\x5a\x53\x20\x00\xc0\x0b\x56\xa7\x93\x2f\x97\x18\xe9\x92\x74\xc0\x48\xb4\x33\x3e\xfb\xc0\x12\xaa\xa7\xd5\xf3\xdc\x5a\x47\x59\x00\xfe\x47\xd2\x44\xb0\x61\x06\x95\x9f\xe6\xea\xec\xe9\xb5\x0c\xd1\xc7\x27\x7d\xd9\xee\xd8\x37\x41\x15\x6b\x1f\x72\xdd\x0d\xac\x60\x82\x6f\x2e\x89\x65\x38\xee\x54\x33\x5b\x6e\x78\x1a\xe6\x8c\x00\xa4\x90\xac\x7f\x6f\xf2\x3b\x93\xa8\x9e\xec\xc8\xb5\xf1\xc5\x55\x8c\x63\x8a\xf4\x06\xd4\x91\xa1\x50\x0d\x36\xf8\xbc\xe8\xfb\xed\xf1\x91\x84\x60\x06\xb0\x51\x26\xe2\xd8\x23\xd1\x90\x89\xfb\x4f\x57\x59\x1d\xf6\xff\xff\x43\xd2\xb3\xcc\xfa\xef\x6b\xa2\x91\x10\x9a\x21\xf3\x91\xbd\x6f\x7f\xd6\x9a\x42\x5b\xf4\xe7\x41\x98\xeb\x37\xc0\xf2\xb7\x01\x33\xa4\x66\x0c\xf9\x4c\x33\x90\x5f\x0e\x98\xfb\x70\x82\xc8\x98\x2f\x40\xd2\x41\x4d\x5a\x56\xad\x7d\x62\x82\x5a\x0b\xbd\x70\x98\xf1\x61\x11\x19\x76\x58\x72\xe4\xd1\x56\xb5\x46\x88\x2d\x6a\x58\x9d\x84\x8c\x49\xad\x2b\xb6\xf4\x0f\x3a\xc9\x54\x57\x95\xa2\x7e\x6c\x46\xc8\xe4\xb7\x7e\x9f\xb0\x9d\x5e\x8e\x92\xf9\x7c\x90\xbf\x2d\x0b\x2d\x31\xcd\x44\xc2\xeb\x8d\xa8\x3b\x41\x4a\xc8\xb9\xc6\xbd\xb4\xa7\xd6\x86\xe7\xe4\x91\xa5\xfe\xa8\x14\xe3\x9c\xc4\xce\xe2\x7e\x30\x1f\xf5\x86\x88\xf3\x37\xf4\xf6\xb7\x06\x07\x50\x9d\x51\xdc\x74\xc9\x42\x5c\x60\x47\x78\x96\x84\xfb\xd9\xae\x43\x5c\x37\x66\x11\xca\x0e\x33\x90\x37\x2f\x17\x77\xf5\xfd\x7f\x4c\xf5\x56\xea\xf5\x6e\x13\xd9\xa4\xa2\x73\xfa\xe2\x37\x4b\xb1\x82\x53\xf1\x3e\x0e\xcb\x8c\x61\xfd\x4c\x20\x94\x9c\x12\xc1\x7d\xfc\xd4\x1b\x83\x12\xc0\xe1\x0b\x60\xb0\xf0\x26\x6a\xbd\x8d\x28\x85\x58\xda\x90\xe1\xd3\x82\x34\xf8\x85\x2d\xc4\x43\xb8\x38\x7a\x3b\x2d\xea\xa8\x8e\x61\xb5\x7b\x93\x96\xd9\x4b\x56\x92\xa0\x38\x38\x6e\x61\x9d\x2c\x8a\xba\xe3\xe7\x35\xe1\xee\xaa\x18\xf0\xb2\xf3\xa4\x5e\xd5\x61\xbd\xc1\xdb\x24\x75\x45\xff\xde\xd3\xd6\x2f\xa0\xd5\x47\x73\xac\x94\xec\x34\xec\x02\x13\x81\x6f\xee\x54\x44\x61\xe2\x77\xb9\xba\xb8\x08\xe0\x7a\xcc\x16\xd0\x01\xe6\xdf\x66\x2e\x1e\x1c\xa5\x1b\x8c\xe6\x01\x74\x4c\xd8\x03\x97\xcd\xc6\x53\x0d\x53\xbc\xad\x17\x5c\x51\x16\x40\x21\x5c\x74\x1d\xa6\x9e\x24\xb6\xc7\x89\xe3"')) 
    send(IP(dst="Server IP")/UDP(dport=443)/Raw(load='"\xc3\x00\x00\x00\x01\x08\x87\x0b\xc3\xb4\x98\x05\x79\x69\x08\x54\x4c\x28\x4e\x7c\x54\x2a\x3d\x00\x44\xe6\x52\x3b\x7e\x2e\x8b\xd2\x93\xf4\x0a\x65\x10\x86\xaf\x12\x97\xc4\x3a\xbd\x16\x53\x1b\x6d\x0c\xd8\x82\xf6\x70\xff\x30\xb6\x9e\x50\xb9\x9e\x6d\xc5\xf3\x7e\x44\xeb\x9a\x10\x12\xd0\x88\xe8\x76\x60\x36\xdc\x2b\x66\x77\xa0\x83\x4e\x52\xab\x83\x0f\x91\xc6\x38\xa4\xec\xf2\xe4\x37\x93\x6f\x9a\xe1\x0f\xc0\x7b\x15\x29\x71\xb3\x3f\xf4\x40\xd6\x6a\xbf\x17\x71\xb7\xcf\x51\xd2\xa6\xef\x8e\x3a\xd8\x0c\xcb\xbb\x50\xc2\xff\x8e\xd4\xaa\x83\xe8\x9c\xef\xd5\x41\xf6\x74\x97\xad\x42\x96\x1c\x42\xa9\xcb\x39\xd6\x9c\xcf\x1a\xa2\x40\xf9\xc3\x72\x27\x49\x9d\xc6\x59\xcf\x51\x34\x11\xa3\x44\x6a\xc6\xb8\x3d\x2d\xda\xbd\x6c\xf1\xb1\xd6\xda\xfd\x09\x03\x4f\xab\x1d\xe4\xa8\x93\x2d\x5f\x36\xcf\x47\x6d\xc6\xa4\x38\x0b\x52\x91\xf4\xb7\x8c\x92\xe4\xf0\xec\xa0\xc2\x89\xba\x1a\xc6\xbf\x21\x28\x21\xea\x6e\x70\xa7\xec\xde\x1a\x29\xf6\x08\xdb\xba\xc1\x3a\xfe\x70\x19\xe3\x13\xb3\x88\x64\xd5\x27\xd2\x84\x88\x71\x28\x79\x84\x33\x06\x70\xed\xfc\x64\xfb\xf1\xed\xac\x98\xdf\x77\x88\x38\x33\xaa\x00\x04\x73\x35\xed\x6e\x08\xaf\x37\x0c\x2f\x33\xb9\xb2\x5b\x5c\x8d\xd4\x05\x3d\xed\x89\x2f\x27\x93\xf4\x0e\x33\x7d\xb7\xc1\x6a\xc5\xa6\x6c\xd5\x4b\x21\x46\xcb\x5b\x5a\xbf\xd7\xd6\xbe\xff\x3b\xc6\x43\x19\x13\x9b\xe3\x1d\xef\xdd\xbf\xfe\x38\x29\x24\xe0\xea\xcc\xdd\xda\xa6\x00\x7e\x6b\x9d\x55\x1f\xc5\x16\x47\x92\xb3\x3c\xd8\x8a\x10\xd7\xd7\x04\x4c\x5c\x79\xa0\x4b\x10\x8e\x92\xec\x31\xe1\x0a\xc9\x4a\xd1\x0e\x49\xd7\xab\xdb\x34\xd0\x6d\x89\x9b\x49\xd5\xe1\x7b\xe8\xe7\x6d\x2d\x0e\xf7\xe7\x49\xd6\x94\xfd\xbe\x9d\xf8\x92\x0c\x23\x31\x2d\x0c\x8d\x6c\x0f\x36\xab\x7a\x4b\xbe\x19\x44\xb5\x38\x16\x6f\x9d\xf3\x2b\x82\x0e\x58\x84\x5f\xae\x2b\x69\x7c\xb1\x5b\x01\xa6\x61\x14\x0e\xf6\xd0\x89\x89\x57\xf4\x37\xde\x10\x72\x0f\xab\x30\x25\xbf\xd3\xc5\x9b\xae\xb2\x0e\x20\x12\xa8\x73\x2d\xb6\xd7\x56\x5b\x94\x8c\x66\x00\x3c\x80\xf8\x15\x24\x65\x59\xc4\x1d\xd9\x8f\x2d\x13\xb7\x3f\xa8\xc2\x14\x54\xc7\x49\xb0\x08\x92\x4d\x95\xd2\x2d\xf3\x89\x14\xd3\x86\x1d\x1a\x1f\xea\x8e\x9d\x23\xef\x06\x92\x16\x23\xd1\x0a\x9e\x24\x7e\xfc\x60\x7b\xac\x3e\x8c\x3d\xcc\xbd\x83\x8e\x95\x35\xcb\xaf\x00\x13\xb5\x9b\xfc\x6c\xb0\x58\x24\xac\xef\x17\xff\xfb\x93\xad\xfe\xcd\x01\xc5\x0a\xad\xa1\x03\x20\x23\xc4\x9b\xb4\x04\xc2\x2a\xe7\x4b\x2b\x1f\x0a\xd6\xa5\xf1\x36\x63\x27\xae\x70\xe1\xe9\xf5\x3d\x9f\x5b\x3a\x77\x0d\x6c\x98\x04\x86\xd6\x6b\xe7\xba\x64\x32\x22\x3d\x5f\x52\x2c\x9b\x5e\x08\x91\x20\xdc\x57\xf7\x6c\x9d\xef\x97\x1b\xf1\xf0\xa9\xf7\x20\xc7\xb5\xba\x0c\x0f\xc4\xda\x23\x3f\xaf\x9e\x77\xee\xfc\x49\x12\xee\xe9\x1c\x0f\x8d\x1d\x62\xff\xeb\x0f\xf5\x9b\x72\xdc\xa7\x93\x1c\xba\xa7\x95\x4d\x4c\xc7\x6a\xae\x69\x5e\xba\x37\xb0\xb3\xea\x6a\x71\x07\x77\xb8\x39\x0d\x01\xb8\x02\xeb\x30\x3b\xf5\x46\x95\xcb\xfa\x3b\x2a\x8d\x5d\x8b\xe4\xab\x46\x91\x16\xbb\xa4\xbc\x90\x08\x24\xaa\x48\x67\xe8\x4e\x2a\xdf\xa3\xae\xc1\xd0\x7f\xac\x86\x2e\x92\xb3\x23\xc0\x39\xd3\xa1\x60\xfc\x02\x95\x05\xc3\x06\x8f\x5e\xc7\x67\xe1\xa3\x58\x46\x43\xf3\x4d\xb3\x95\xf9\xa8\x94\x69\xc0\xa2\x02\x6b\x39\x1d\xa7\xe6\xe0\xc6\x4c\x3f\x1c\x0d\xde\x89\x33\x57\x65\x5e\xbf\xe8\xae\x58\x7f\xfe\x41\x06\x16\x5a\x53\x20\x00\xc0\x0b\x56\xa7\x93\x2f\x97\x18\xe9\x92\x74\xc0\x48\xb4\x33\x3e\xfb\xc0\x12\xaa\xa7\xd5\xf3\xdc\x5a\x47\x59\x00\xfe\x47\xd2\x44\xb0\x61\x06\x95\x9f\xe6\xea\xec\xe9\xb5\x0c\xd1\xc7\x27\x7d\xd9\xee\xd8\x37\x41\x15\x6b\x1f\x72\xdd\x0d\xac\x60\x82\x6f\x2e\x89\x65\x38\xee\x54\x33\x5b\x6e\x78\x1a\xe6\x8c\x00\xa4\x90\xac\x7f\x6f\xf2\x3b\x93\xa8\x9e\xec\xc8\xb5\xf1\xc5\x55\x8c\x63\x8a\xf4\x06\xd4\x91\xa1\x50\x0d\x36\xf8\xbc\xe8\xfb\xed\xf1\x91\x84\x60\x06\xb0\x51\x26\xe2\xd8\x23\xd1\x90\x89\xfb\x4f\x57\x59\x1d\xf6\xff\xff\x43\xd2\xb3\xcc\xfa\xef\x6b\xa2\x91\x10\x9a\x21\xf3\x91\xbd\x6f\x7f\xd6\x9a\x42\x5b\xf4\xe7\x41\x98\xeb\x37\xc0\xf2\xb7\x01\x33\xa4\x66\x0c\xf9\x4c\x33\x90\x5f\x0e\x98\xfb\x70\x82\xc8\x98\x2f\x40\xd2\x41\x4d\x5a\x56\xad\x7d\x62\x82\x5a\x0b\xbd\x70\x98\xf1\x61\x11\x19\x76\x58\x72\xe4\xd1\x56\xb5\x46\x88\x2d\x6a\x58\x9d\x84\x8c\x49\xad\x2b\xb6\xf4\x0f\x3a\xc9\x54\x57\x95\xa2\x7e\x6c\x46\xc8\xe4\xb7\x7e\x9f\xb0\x9d\x5e\x8e\x92\xf9\x7c\x90\xbf\x2d\x0b\x2d\x31\xcd\x44\xc2\xeb\x8d\xa8\x3b\x41\x4a\xc8\xb9\xc6\xbd\xb4\xa7\xd6\x86\xe7\xe4\x91\xa5\xfe\xa8\x14\xe3\x9c\xc4\xce\xe2\x7e\x30\x1f\xf5\x86\x88\xf3\x37\xf4\xf6\xb7\x06\x07\x50\x9d\x51\xdc\x74\xc9\x42\x5c\x60\x47\x78\x96\x84\xfb\xd9\xae\x43\x5c\x37\x66\x11\xca\x0e\x33\x90\x37\x2f\x17\x77\xf5\xfd\x7f\x4c\xf5\x56\xea\xf5\x6e\x13\xd9\xa4\xa2\x73\xfa\xe2\x37\x4b\xb1\x82\x53\xf1\x3e\x0e\xcb\x8c\x61\xfd\x4c\x20\x94\x9c\x12\xc1\x7d\xfc\xd4\x1b\x83\x12\xc0\xe1\x0b\x60\xb0\xf0\x26\x6a\xbd\x8d\x28\x85\x58\xda\x90\xe1\xd3\x82\x34\xf8\x85\x2d\xc4\x43\xb8\x38\x7a\x3b\x2d\xea\xa8\x8e\x61\xb5\x7b\x93\x96\xd9\x4b\x56\x92\xa0\x38\x38\x6e\x61\x9d\x2c\x8a\xba\xe3\xe7\x35\xe1\xee\xaa\x18\xf0\xb2\xf3\xa4\x5e\xd5\x61\xbd\xc1\xdb\x24\x75\x45\xff\xde\xd3\xd6\x2f\xa0\xd5\x47\x73\xac\x94\xec\x34\xec\x02\x13\x81\x6f\xee\x54\x44\x61\xe2\x77\xb9\xba\xb8\x08\xe0\x7a\xcc\x16\xd0\x01\xe6\xdf\x66\x2e\x1e\x1c\xa5\x1b\x8c\xe6\x01\x74\x4c\xd8\x03\x97\xcd\xc6\x53\x0d\x53\xbc\xad\x17\x5c\x51\x16\x40\x21\x5c\x74\x1d\xa6\x9e\x24\xb6\xc7\x89\xe3"'))  
