top = '.'
out = 'build'
APPNAME = 'foo'
VERSION = '0.0'

def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.load('compiler_cxx protoc')

def build(bld):
    bld(name='codegenInclude', export_includes='codegen_include')
    bld(features='cxx', source='Foo.proto', target='Foo',
        use=['PROTOBUF'], includes=['.'])
    bld.recurse('bar')

# Have all 'cxx' targets have 'codegen_include' in their include paths.
from waflib import TaskGen
@TaskGen.taskgen_method
@TaskGen.feature('cxx')
def add_include(self):
    self.use = self.to_list(getattr(self, 'use', [])) + ['codegenInclude']
