# AUTOGENERATED DON'T EDIT
# Please make changes to the code generator             (distutils/ccompiler_opt.py)
hash = 2407312721
data = \
{'cache_infile': True,
 'cache_me': {"('cc_test_flags', ['-O3'])": True,
              "('cc_test_flags', ['-Werror'])": True,
              "('cc_test_flags', ['-march=native'])": False,
              "('cc_test_flags', ['-mfpu=neon'])": True,
              "('cc_test_flags', ['-mfpu=neon-fp-armv8', '-march=armv8-a+simd'])": False,
              "('cc_test_flags', ['-mfpu=neon-fp16', '-mfp16-format=ieee'])": False,
              "('cc_test_flags', ['-mfpu=neon-vfpv4'])": True,
              "('feature_extra_checks', 'NEON')": [],
              "('feature_flags', 'ASIMD')": ['-mfpu=neon-vfpv4'],
              "('feature_flags', 'NEON')": ['-mfpu=neon'],
              "('feature_flags', 'NEON_FP16')": ['-mfpu=neon'],
              "('feature_flags', 'NEON_VFPV4')": ['-mfpu=neon-vfpv4'],
              "('feature_flags', set())": [],
              "('feature_is_supported', 'ASIMD', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'ASIMDDP', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'ASIMDFHM', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'ASIMDHP', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'NEON', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'NEON_FP16', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'NEON_VFPV4', 'force_flags', 'macros', None, [])": False,
              "('feature_test', 'ASIMD', None, 'macros', [])": False,
              "('feature_test', 'NEON', None, 'macros', [])": True,
              "('feature_test', 'NEON_FP16', None, 'macros', [])": False,
              "('feature_test', 'NEON_VFPV4', None, 'macros', [])": True},
 'cache_private': {'sources_status'},
 'cc_flags': {'native': [], 'opt': ['-O3'], 'werror': ['-Werror']},
 'cc_has_debug': False,
 'cc_has_native': False,
 'cc_is_cached': True,
 'cc_is_clang': False,
 'cc_is_gcc': True,
 'cc_is_icc': False,
 'cc_is_iccw': False,
 'cc_is_msvc': False,
 'cc_is_nocc': True,
 'cc_march': 'armhf',
 'cc_name': 'gcc',
 'cc_noopt': False,
 'cc_on_aarch64': False,
 'cc_on_armhf': True,
 'cc_on_noarch': False,
 'cc_on_ppc64': False,
 'cc_on_ppc64le': False,
 'cc_on_x64': False,
 'cc_on_x86': False,
 'feature_is_cached': True,
 'feature_min': set(),
 'feature_supported': {'ASIMD': {'flags': ['-mfpu=neon-fp-armv8',
                                           '-march=armv8-a+simd'],
                                 'implies': ['NEON_FP16', 'NEON_VFPV4'],
                                 'implies_detect': False,
                                 'interest': 4},
                       'ASIMDDP': {'flags': ['-march=armv8.2-a+dotprod'],
                                   'implies': ['ASIMD'],
                                   'interest': 6},
                       'ASIMDFHM': {'flags': ['-march=armv8.2-a+fp16fml'],
                                    'implies': ['ASIMDHP'],
                                    'interest': 7},
                       'ASIMDHP': {'flags': ['-march=armv8.2-a+fp16'],
                                   'implies': ['ASIMD'],
                                   'interest': 5},
                       'NEON': {'flags': ['-mfpu=neon'],
                                'headers': ['arm_neon.h'],
                                'interest': 1},
                       'NEON_FP16': {'flags': ['-mfpu=neon-fp16',
                                               '-mfp16-format=ieee'],
                                     'implies': ['NEON'],
                                     'interest': 2},
                       'NEON_VFPV4': {'flags': ['-mfpu=neon-vfpv4'],
                                      'implies': ['NEON_FP16'],
                                      'interest': 3}},
 'hit_cache': True,
 'parse_baseline_flags': [],
 'parse_baseline_names': [],
 'parse_dispatch_names': ['NEON'],
 'parse_is_cached': True,
 'parse_target_groups': {'SIMD_TEST': (True, ['NEON'], [])},
 'sources_status': {}}