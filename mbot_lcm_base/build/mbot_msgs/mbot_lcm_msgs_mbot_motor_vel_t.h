// THIS IS AN AUTOMATICALLY GENERATED FILE.  DO NOT MODIFY
// BY HAND!!
//
// Generated by lcm-gen

#ifndef _mbot_lcm_msgs_mbot_motor_vel_t_h
#define _mbot_lcm_msgs_mbot_motor_vel_t_h

#include <stdint.h>
#include <stdlib.h>
#include <lcm/lcm_coretypes.h>
#include <lcm/lcm.h>
#include "mbot_lcm_msgs_export.h"

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Motor velocity command for the 3 motors
 * on the MBot Control Board
 */
typedef struct _mbot_lcm_msgs_mbot_motor_vel_t mbot_lcm_msgs_mbot_motor_vel_t;
struct _mbot_lcm_msgs_mbot_motor_vel_t
{
    int64_t    utime;
    float      velocity[3];
};

/**
 * Create a deep copy of a mbot_lcm_msgs_mbot_motor_vel_t.
 * When no longer needed, destroy it with mbot_lcm_msgs_mbot_motor_vel_t_destroy()
 */
MBOT_LCM_MSGS_EXPORT mbot_lcm_msgs_mbot_motor_vel_t* mbot_lcm_msgs_mbot_motor_vel_t_copy(const mbot_lcm_msgs_mbot_motor_vel_t* to_copy);

/**
 * Destroy an instance of mbot_lcm_msgs_mbot_motor_vel_t created by mbot_lcm_msgs_mbot_motor_vel_t_copy()
 */
MBOT_LCM_MSGS_EXPORT void mbot_lcm_msgs_mbot_motor_vel_t_destroy(mbot_lcm_msgs_mbot_motor_vel_t* to_destroy);

/**
 * Identifies a single subscription.  This is an opaque data type.
 */
typedef struct _mbot_lcm_msgs_mbot_motor_vel_t_subscription_t mbot_lcm_msgs_mbot_motor_vel_t_subscription_t;

/**
 * Prototype for a callback function invoked when a message of type
 * mbot_lcm_msgs_mbot_motor_vel_t is received.
 */
typedef void(*mbot_lcm_msgs_mbot_motor_vel_t_handler_t)(
    const lcm_recv_buf_t *rbuf, const char *channel,
    const mbot_lcm_msgs_mbot_motor_vel_t *msg, void *userdata);

/**
 * Publish a message of type mbot_lcm_msgs_mbot_motor_vel_t using LCM.
 *
 * @param lcm The LCM instance to publish with.
 * @param channel The channel to publish on.
 * @param msg The message to publish.
 * @return 0 on success, <0 on error.  Success means LCM has transferred
 * responsibility of the message data to the OS.
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_publish(lcm_t *lcm, const char *channel, const mbot_lcm_msgs_mbot_motor_vel_t *msg);

/**
 * Subscribe to messages of type mbot_lcm_msgs_mbot_motor_vel_t using LCM.
 *
 * @param lcm The LCM instance to subscribe with.
 * @param channel The channel to subscribe to.
 * @param handler The callback function invoked by LCM when a message is
 *     received. This function is invoked by LCM during calls to lcm_handle()
 *     and lcm_handle_timeout().
 * @param userdata An opaque pointer passed to @p handler when it is invoked.
 * @return 0 on success, <0 if an error occured
 */
MBOT_LCM_MSGS_EXPORT mbot_lcm_msgs_mbot_motor_vel_t_subscription_t* mbot_lcm_msgs_mbot_motor_vel_t_subscribe(
    lcm_t *lcm, const char *channel, mbot_lcm_msgs_mbot_motor_vel_t_handler_t handler, void *userdata);

/**
 * Removes and destroys a subscription created by mbot_lcm_msgs_mbot_motor_vel_t_subscribe()
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_unsubscribe(lcm_t *lcm, mbot_lcm_msgs_mbot_motor_vel_t_subscription_t* hid);

/**
 * Sets the queue capacity for a subscription.
 * Some LCM providers (e.g., the default multicast provider) are implemented
 * using a background receive thread that constantly revceives messages from
 * the network.  As these messages are received, they are buffered on
 * per-subscription queues until dispatched by lcm_handle().  This function
 * how many messages are queued before dropping messages.
 *
 * @param subs the subscription to modify.
 * @param num_messages The maximum number of messages to queue
 *  on the subscription.
 * @return 0 on success, <0 if an error occured
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_subscription_set_queue_capacity(
    mbot_lcm_msgs_mbot_motor_vel_t_subscription_t* subs, int num_messages);

/**
 * Encode a message of type mbot_lcm_msgs_mbot_motor_vel_t into binary form.
 *
 * @param buf The output buffer.
 * @param offset Encoding starts at this byte offset into @p buf.
 * @param maxlen Maximum number of bytes to write.  This should generally
 *               be equal to mbot_lcm_msgs_mbot_motor_vel_t_encoded_size().
 * @param msg The message to encode.
 * @return The number of bytes encoded, or <0 if an error occured.
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_encode(void *buf, int offset, int maxlen, const mbot_lcm_msgs_mbot_motor_vel_t *p);

/**
 * Decode a message of type mbot_lcm_msgs_mbot_motor_vel_t from binary form.
 * When decoding messages containing strings or variable-length arrays, this
 * function may allocate memory.  When finished with the decoded message,
 * release allocated resources with mbot_lcm_msgs_mbot_motor_vel_t_decode_cleanup().
 *
 * @param buf The buffer containing the encoded message
 * @param offset The byte offset into @p buf where the encoded message starts.
 * @param maxlen The maximum number of bytes to read while decoding.
 * @param msg Output parameter where the decoded message is stored
 * @return The number of bytes decoded, or <0 if an error occured.
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_decode(const void *buf, int offset, int maxlen, mbot_lcm_msgs_mbot_motor_vel_t *msg);

/**
 * Release resources allocated by mbot_lcm_msgs_mbot_motor_vel_t_decode()
 * @return 0
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_decode_cleanup(mbot_lcm_msgs_mbot_motor_vel_t *p);

/**
 * Check how many bytes are required to encode a message of type mbot_lcm_msgs_mbot_motor_vel_t
 */
MBOT_LCM_MSGS_EXPORT int mbot_lcm_msgs_mbot_motor_vel_t_encoded_size(const mbot_lcm_msgs_mbot_motor_vel_t *p);

// LCM support functions. Users should not call these
MBOT_LCM_MSGS_EXPORT int64_t __mbot_lcm_msgs_mbot_motor_vel_t_get_hash(void);
MBOT_LCM_MSGS_EXPORT uint64_t __mbot_lcm_msgs_mbot_motor_vel_t_hash_recursive(const __lcm_hash_ptr *p);
MBOT_LCM_MSGS_EXPORT int __mbot_lcm_msgs_mbot_motor_vel_t_encode_array(
    void *buf, int offset, int maxlen, const mbot_lcm_msgs_mbot_motor_vel_t *p, int elements);
MBOT_LCM_MSGS_EXPORT int __mbot_lcm_msgs_mbot_motor_vel_t_decode_array(
    const void *buf, int offset, int maxlen, mbot_lcm_msgs_mbot_motor_vel_t *p, int elements);
MBOT_LCM_MSGS_EXPORT int __mbot_lcm_msgs_mbot_motor_vel_t_decode_array_cleanup(mbot_lcm_msgs_mbot_motor_vel_t *p, int elements);
MBOT_LCM_MSGS_EXPORT int __mbot_lcm_msgs_mbot_motor_vel_t_encoded_array_size(const mbot_lcm_msgs_mbot_motor_vel_t *p, int elements);
MBOT_LCM_MSGS_EXPORT int __mbot_lcm_msgs_mbot_motor_vel_t_clone_array(const mbot_lcm_msgs_mbot_motor_vel_t *p, mbot_lcm_msgs_mbot_motor_vel_t *q, int elements);

#ifdef __cplusplus
}
#endif

#endif
