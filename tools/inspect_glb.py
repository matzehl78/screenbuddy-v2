#!/usr/bin/env python3
"""Inspect a binary GLB model without changing its geometry or animations."""
import json,struct,sys
from pathlib import Path

def inspect(path):
    data=Path(path).read_bytes()
    if len(data)<20 or data[:4]!=b'glTF':
        raise ValueError("Not a binary GLB file")
    version,length=struct.unpack_from('<II',data,4)
    if version!=2 or length!=len(data):
        raise ValueError("Unsupported or truncated GLB")
    offset=12
    gltf=None
    while offset+8<=len(data):
        size,kind=struct.unpack_from('<I4s',data,offset)
        offset+=8
        if offset+size>len(data):raise ValueError("Invalid GLB chunk size")
        if kind==b'JSON':gltf=json.loads(data[offset:offset+size].decode('utf-8'))
        offset+=size
    if gltf is None:raise ValueError("Missing GLB JSON chunk")
    print("FILE:",path)
    print("NODES:")
    for i,n in enumerate(gltf.get('nodes',[])):
        print(f"  {i}: {n.get('name','(unnamed)')} mesh={n.get('mesh')} children={n.get('children',[])}")
    print("MESHES:")
    for i,m in enumerate(gltf.get('meshes',[])):
        print(f"  {i}: {m.get('name','(unnamed)')} primitives={len(m.get('primitives',[]))}")
    print("ANIMATIONS:")
    for a in gltf.get('animations',[]):
        print(" ",a.get('name','(unnamed)'),[(c.get('target',{}).get('node'),c.get('target',{}).get('path')) for c in a.get('channels',[])])
    print("MATERIALS:",[m.get('name','(unnamed)') for m in gltf.get('materials',[])])
    print("NOTE: This report alone cannot establish whether the torso is a separate mesh.")

if __name__=='__main__':
    if len(sys.argv)<2:raise SystemExit("Usage: python tools/inspect_glb.py models/neonbot_idle.glb")
    for p in sys.argv[1:]:inspect(p)
