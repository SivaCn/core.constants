# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
from string import Template
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #


__all__ = [
    # All public symbols go here.
]

message_mapper = {
  'CM0001' : 'Invalid username/password',
  'CM0002' : 'User $user_name successfully created' ,
  'CM0003' : 'User Already exists',
  'CM0004' : 'Error while verifying the OTP',
  'CM0005' : 'OTP does not match !',
  'CM0006' : 'Data saved successfully',
  'CM0007' : 'Data updated successfully',
  'CM0008' : 'Invalid Date. Please select valid date',
  'CM0009' : 'Deactivated successfully',
  'CM0010' : 'Successfully Started the Scheduler Service',
  'CM0011' : 'Unable to Start the Scheduler Service',
  'CM0012' : 'Shutting Down the Scheduler Service',
  'CM0013' : 'Unable to Shutdown the Scheduler Service',
  'CM0014' : 'Successfully Scheduled.',
  'CM0015' : 'Message broker is not reachable.',
  'CM0016' : 'Job does not available for deactivation',
  'CM0017' : 'Successfully deactivated the job.',
  'CM0018' : 'Successfully Updated.',
  'CM0019' : 'Please use $otp_code as one time password',
  'CM0020' : 'Password Successfully Changed',
  'CM0021' : 'Scheduled $schedule_type Job initiated at $current_datetime',
  'CM0022' : 'EVENT_JOB_ADDED: Added job with job_id: $job_id',
  'CM0023' : 'EVENT_JOB_MODIFIED: Updated job with job_id: $job_id to run at: $next_run_time',
  'CM0024' : 'EVENT_JOB_REMOVED: Removed job with job_id: $job_id',
  'CM0025' : 'EVENT_JOB_EXECUTED: Scheduled job with job_id: $job_id at: $next_run_time was executed !',
  'CM0026' : 'EVENT_JOB_MISSED: Scheduled job with job_id: $job_id at: $next_run_time was missed !',
  'CM0027' : 'EVENT_JOB_ERROR: Scheduled job with job_id: $job_id at: $next_run_time was failed !',
  'CM0028' : 'Job with job_id: $job_id already exists',
  'CM0029' : 'Successfully scheduled $schedule_type job',
  'CM0030' : 'Argument job_action is not one among $allowed_job_actions',
  'CM0031' : 'Unable to remove job with job_id($job_id)',
  'CM0032' : 'Successfully removed the job with job_id($job_id)',
  'CM0033' : 'No job found with job_id($job_id)',
  'CM0034' : 'No failed sms found',
 }

def code_message(code):
    return message_mapper.get(code, 'No message configured for the code: {}'.format(code))

def filled_code_message(code, **kwargs):
    if not kwargs:
        return code_message(code)

    return Template(code_message(code)).safe_substitute(kwargs)




