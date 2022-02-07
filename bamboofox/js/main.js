(() => {
  const fail = () => {
    alert('No');
    document.querySelector('#username').value = '';
    document.querySelector('#password').value = '';
    return true;
  };

  const success = (flag) => {
    alert(`Welcome back, admin!
Here is your flag: ${flag}`);
    return true;
  }

  document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;

    if (username !== 'admin') {
      fail();
    } else {
      const target = '\x48\x4a\x45\x45\x41\x40\x46\x3e\x4a\x68\x62\x6d\x2e\x57\x70\x2a\x54\x5d\x43\x69\x2a\x51\x25\x57\x26\x65\x21\x1f\x48\x5a';
      let cnt = 0;
      let flag = '';

      for (let i = 0; i < target.length; i++) {
          flag += String.fromCharCode(target.charCodeAt(i) + 10 + i);
      }
      console.log('flag' + flag);

      for (let i = 0; i < target.length; i++) {
        cnt += password.charCodeAt(i) - 10 - i == target.charCodeAt(i);
        if (password.charCodeAt(i) - 10 - i == target.charCodeAt(i)) {
          console.log(password[i]);
        }
      }

      cnt == target.length && success(password);
    }
  })
})();
