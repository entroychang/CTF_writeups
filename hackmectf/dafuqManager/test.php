<?php
function make_command($cmd) {
    $hmac = hash_hmac('sha256', $cmd, 'KHomg4WfVeJNj9q5HFcWr5kc8XzE4PyzB8brEw6pQQyzmIZuRBbwDU7UE6jYjPm3');
    return sprintf('%s.%s', base64_encode($cmd), $hmac);
}

$command = make_command("('sys'.'tem')('ls -al ../../tmp');");
list($cmd, $hmac) = explode('.', $command, 2);
$cmd = base64_decode($cmd);
// echo $cmd;
// (eval($cmd));
$bad_things = array('system', 'exec', 'popen', 'pcntl_exec', 'proc_open', 'passthru', '`', 'eval', 'assert', 'preg_replace', 'create_function', 'include', 'require', 'curl',);
foreach ($bad_things as $bad) {
    if (stristr($cmd, $bad)) {
        die('2bad');
    }
}
if (hash_equals(hash_hmac('sha256', $cmd, 'KHomg4WfVeJNj9q5HFcWr5kc8XzE4PyzB8brEw6pQQyzmIZuRBbwDU7UE6jYjPm3'), $hmac)) {
    // die(eval($cmd));
} else {
    echo('What does the fox say?');
}