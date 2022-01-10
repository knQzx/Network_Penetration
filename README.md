<h1>The program for the pentest</h1>
<h2>Functions of this program: </h2>
<ul>
    <li>view all IP addresses on your local network</li>
    <li>view all open\closed ports for these ip</li>
    <li>trial brute force of ssh passwords (if you have a PC on the network that has ssh open (port 22))</li>
</ul>
<h2>The order of actions performed: </h2>
<ol>
    <li>Change the language to English and make sure that you have nmap, hydra and requirements.txt . Linux needs an operating system.</li>
    <li>Initially, you should run the file "scan_ip's.py ". It will write all the ip addresses found on the network to a file.</li>
    <li>Then you have to run the file "brutforce_ssh.py ". It will look at all open ports on these ip addresses and write it to a file.</li>
    <li>And finally you have to run "brutforce_ssh.py " and wait for a while, and if he can pick up the password, then everything will be successful.</li>
</ol>
<p>Thanks to all those who created nmap and hydra. This script does not encourage you to use it for bad purposes.</p>