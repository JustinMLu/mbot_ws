
#ifndef MBOT_LCM_MSGS_EXPORT_H
#define MBOT_LCM_MSGS_EXPORT_H

#ifdef MBOT_LCM_MSGS_STATIC_DEFINE
#  define MBOT_LCM_MSGS_EXPORT
#  define MBOT_LCM_MSGS_NO_EXPORT
#else
#  ifndef MBOT_LCM_MSGS_EXPORT
#    ifdef mbot_lcm_msgs_EXPORTS
        /* We are building this library */
#      define MBOT_LCM_MSGS_EXPORT 
#    else
        /* We are using this library */
#      define MBOT_LCM_MSGS_EXPORT 
#    endif
#  endif

#  ifndef MBOT_LCM_MSGS_NO_EXPORT
#    define MBOT_LCM_MSGS_NO_EXPORT 
#  endif
#endif

#ifndef MBOT_LCM_MSGS_DEPRECATED
#  define MBOT_LCM_MSGS_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef MBOT_LCM_MSGS_DEPRECATED_EXPORT
#  define MBOT_LCM_MSGS_DEPRECATED_EXPORT MBOT_LCM_MSGS_EXPORT MBOT_LCM_MSGS_DEPRECATED
#endif

#ifndef MBOT_LCM_MSGS_DEPRECATED_NO_EXPORT
#  define MBOT_LCM_MSGS_DEPRECATED_NO_EXPORT MBOT_LCM_MSGS_NO_EXPORT MBOT_LCM_MSGS_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef MBOT_LCM_MSGS_NO_DEPRECATED
#    define MBOT_LCM_MSGS_NO_DEPRECATED
#  endif
#endif

#endif /* MBOT_LCM_MSGS_EXPORT_H */
