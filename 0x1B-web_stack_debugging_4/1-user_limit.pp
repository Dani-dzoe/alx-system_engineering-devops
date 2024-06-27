Here is the equivalent configuration written in Puppet:
```
class holberton {
  user { 'holberton':
    ensure => present,
    password => 'password',
    groups => ['sudo'],
  }

  package { 'puppet-lint':
    ensure => installed,
  }

  file { '/home/holberton/example.pp':
    ensure => present,
    owner => 'holberton',
    group => 'holberton',
  }

  exec { 'run-puppet-lint':
    command => 'puppet-lint /home/holberton/example.pp',
    user => 'holberton',
  }
}
