@ cdecl spifns_getvarlist(ptr ptr)
@ cdecl spifns_init()
@ cdecl spifns_getvar(ptr)
@ cdecl spifns_get_last_error(ptr ptr)
@ cdecl spifns_set_debug_callback(ptr)
@ cdecl spifns_get_version()
@ cdecl spifns_open_port(long)
@ cdecl spifns_close_port()
@ varargs spifns_debugout(ptr)
@ cdecl spifns_close()
@ cdecl spifns_chip_select(long)
@ cdecl spifns_command(str)
@ cdecl spifns_enumerate_ports(ptr ptr)
@ cdecl spifns_sequence_setvar_spishiftperiod(long)
@ cdecl spifns_sequence_setvar_spiport(long)
@ cdecl spifns_debugout_readwrite(long long long ptr)
@ cdecl spifns_sequence_write(long long ptr)
@ cdecl spifns_sequence_setvar_spimul(long)
@ cdecl spifns_sequence_setvar(str str)
@ cdecl spifns_sequence_read(long long ptr)
@ cdecl spifns_sequence(ptr long)
@ cdecl spifns_bluecore_xap_stopped()
