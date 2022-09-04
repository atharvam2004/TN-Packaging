<?php
include('smtp/PHPMailerAutoload.php');

$html='Msg';

   
$name = strip_tags(htmlspecialchars($_POST['name']));
$email_address = strip_tags(htmlspecialchars($_POST['email']));
$phone = strip_tags(htmlspecialchars($_POST['phone']));
$message = strip_tags(htmlspecialchars($_POST['message']));

$to = "$email_address"; 
$email_subject = "Website Contact Form:  $name";
$email_body = "You have received a new message from your website contact form.<br><br>"."Here are the details:<br> Name: $name <br> Email: $email_address<br> Phone: $phone<br> Message:\n$message";
$subject = "Contact Form";

echo smtp_mailer('nemade@tnpackaging.com',$subject,$email_body);
function smtp_mailer($to,$subject,$email_body){
	$mail = new PHPMailer(); 
	//$mail->SMTPDebug  = 3;
	$mail->isSMTP();
    $mail->Host = 'localhost';
    $mail->SMTPAuth = false;
    $mail->SMTPAutoTLS = false; 
    $mail->Port = 25; 
	
	$mail->IsHTML(true);
	$mail->CharSet = 'UTF-8';
	$mail->Username = "admin@tnpackaging.com";
	$mail->Password = "admintnpackaging";
	$mail->SetFrom("nemade@tnpackaging.com");

	$mail->Subject = $subject;
	$mail->Body =$email_body;
	$mail->AddAddress($to);
	$mail->SMTPOptions=array('ssl'=>array(
		'verify_peer'=>false,
		'verify_peer_name'=>false,
		'allow_self_signed'=>false
	));
	if(!$mail->Send()){
		echo $mail->ErrorInfo;
	}else{
		return 'Sent';
	}
}
?>