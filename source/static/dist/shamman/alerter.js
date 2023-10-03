
class Alerter {

	static success(title, message, timeOut = 3000) {
		console.log(title, message, timeOut);
		Loader.stop();
		toastr.options = {
			closeButton: true,
			progressBar: true,
			showMethod: 'slideDown',
			timeOut: timeOut
		};
		toastr.success(message, title);
	}


	static warning(title, message){
		toastr.options = {
			closeButton: true,
			progressBar: true,
			showMethod: 'slideDown',
			timeOut: 3000
		};
		toastr.warning(message, title);
	}


	static error(title, message){
		Loader.stop();
		toastr.options = {
			closeButton: true,
			progressBar: true,
			showMethod: 'slideDown',
			timeOut: 3000
		};
		toastr.error(message, title);
	}

}