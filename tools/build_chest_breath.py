#!/usr/bin/env python3
"""Add a gentle looping scale animation to the independent chest_core GLB node."""
import json,struct,sys
from pathlib import Path

def pad(data,fill):return data+fill*((-len(data))%4)

def build(source,destination):
    raw=Path(source).read_bytes()
    if raw[:4]!=b'glTF' or struct.unpack_from('<I',raw,4)[0]!=2:raise ValueError('Expected GLB v2')
    pos=12; chunks=[]
    while pos<len(raw):
        size,typ=struct.unpack_from('<I4s',raw,pos);pos+=8
        chunks.append((typ,raw[pos:pos+size]));pos+=size
    doc=json.loads(next(v for k,v in chunks if k==b'JSON').decode('utf-8'))
    nodes=doc['nodes']; ids=[i for i,n in enumerate(nodes) if n.get('name')=='chest_core']
    if len(ids)!=1:raise ValueError('Expected exactly one chest_core node')
    node=ids[0]
    binary=bytearray(next((v for k,v in chunks if k==b'BIN\x00'),b''))
    # A dedicated scale animation, leaving the body, head, and mouth untouched.
    times=[0.,2.2,4.4]; scales=[1.,1.,1.,1.06,1.06,1.06,1.,1.,1.]
    def accessor(values,kind,count,atype):
        offset=len(binary)
        binary.extend(struct.pack('<'+kind*len(values),*values))
        binary.extend(b'\x00'*((-len(binary))%4))
        view=len(doc.setdefault('bufferViews',[]))
        doc['bufferViews'].append({'buffer':0,'byteOffset':offset,'byteLength':len(values)*4})
        idx=len(doc.setdefault('accessors',[]))
        doc['accessors'].append({'bufferView':view,'componentType':5126,'count':count,'type':atype})
        return idx
    t=accessor(times,'f',3,'SCALAR')
    v=accessor(scales,'f',3,'VEC3')
    doc.setdefault('animations',[]).append({'name':'Chest_Breathe','samplers':[{'input':t,'output':v,'interpolation':'LINEAR'}],'channels':[{'sampler':0,'target':{'node':node,'path':'scale'}}]})
    if len(doc.get('buffers',[]))!=1:raise ValueError('Expected one binary buffer')
    doc['buffers'][0]['byteLength']=len(binary)
    js=pad(json.dumps(doc,separators=(',',':')).encode(),' '.encode())
    binchunk=pad(bytes(binary),b'\x00')
    output=b'glTF'+struct.pack('<II',2,12+8+len(js)+8+len(binchunk))+struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(binchunk),b'BIN\x00')+binchunk
    Path(destination).write_bytes(output)
    print('Built',destination,'chest node',node,'bytes',len(output))
if __name__=='__main__':build(*sys.argv[1:3])
