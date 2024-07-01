# Execute a command
exec { 'killmenow':
  command => 'usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
