window.Superlists = {};
window.Superlists.initialize = function () {
	console.log('initialize called');
	$('input[name="text"]').on('keypress', function () {
		console.log('in keyress handler');
		$('.has-error').hide();
	});
};