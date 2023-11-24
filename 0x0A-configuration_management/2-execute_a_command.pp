# kills a process named killmenow using Puppet

exec { 'kill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/'
}
