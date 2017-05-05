{
    'variables': {
        'platform': '<(OS)',
    },
    "targets": [{
        "target_name": "zookeeper",
        'dependencies': ['libzk'],
        "sources": ["src/node-zk.cpp"],
        'cflags': ['-Wall', '-O0'],
        'conditions': [
            ['OS=="solaris"', {
                'cflags': ['-Wno-strict-aliasing'],
                'defines': ['_POSIX_PTHREAD_SEMANTICS'],
                'include_dirs': [
                    '/opt/local/include/zookeeper',
                    '<!(node -e "require(\'nan\')")'
                ],
	            'ldflags': ['-lzookeeper_st'],
            }],
            ['OS=="mac"',{
                'include_dirs': [
                    '<(module_root_dir)/deps/zookeeper/src/c/include',
                    '<(module_root_dir)/deps/zookeeper/src/c/generated',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['<(module_root_dir)/deps/zookeeper/src/c/.libs/libzookeeper_st.a'],
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                }
            }],['OS=="linux"',{
                'include_dirs': [
                    '<(module_root_dir)/deps/zookeeper/src/c/include',
                    '<(module_root_dir)/deps/zookeeper/src/c/generated',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['<(module_root_dir)/deps/zookeeper/src/c/.libs/libzookeeper_st.a'],
            }],['OS=="win"',{
                'defines': [ 'USE_STATIC_LIB' ], 
                'include_dirs': [
                    '<(module_root_dir)/deps/zookeeper/src/c/include',
                    '<(module_root_dir)/deps/zookeeper/src/c/generated',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['<(module_root_dir)/deps/zookeeper/src/c/libs/$(Platform)/$(Configuration)/libzookeeper.lib'],
            }]
        ]},
        {
            'target_name': 'libzk',
            'type': 'none',
            'conditions': [
                ['OS!="win"', {
                    'actions': [{
                        'action_name': 'build_zk_client_lib',
                        'inputs': [''],
                        'outputs': [''],
                        'action': ['sh', 'scripts/build.sh']
                    }]
                }], ['OS=="win"', {
                    'actions': [{
                        'action_name': 'build_zk_client_lib',
                        'inputs': [''],
                        'outputs': [''],
                        'action': ['powershell.exe', '-f', 'scripts\\build.ps1', '$(Platform)', '$(Configuration)']
                    }]
                }]
            ]
        },
        {
            "target_name": "after_build",
            "type": "none",
            "dependencies": ["zookeeper"],
            'conditions': [
                ['OS!="win"', {
                    "actions": [{
                        "action_name": "symlink",
                        "inputs": ["<@(PRODUCT_DIR)/zookeeper.node"],
                        "outputs": ["<(module_root_dir)/build/zookeeper.node"],
                        "action": ["sh", "scripts/symlink.sh", "<@(_inputs)"]
                    }]
                }], ['OS=="win"', {
                    "actions": [{
                        "action_name": "symlink",
                        "inputs": ["<@(PRODUCT_DIR)/zookeeper.node"],
                        "outputs": ["<(module_root_dir)/build/zookeeper.node"],
                        "action": ['powershell.exe', '-f', 'scripts\\symlink.ps1', '$(Configuration)']
                    }]
                }]
            ]
    }],
}
