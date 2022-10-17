$(function () {
	'use strict'

	// ______________ PAGE LOADING
	$("#global-loader").fadeOut("slow");

	
	
	// ______________ Card
	const DIV_CARD = 'div.card';

	// ______________ Function for remove card
	$(document).on('click', '[data-bs-toggle="card-remove"]', function (e) {
		let $card = $(this).closest(DIV_CARD);
		$card.remove();
		e.preventDefault();
		return false;
	});

	// ______________ Functions for collapsed card
	$(document).on('click', '[data-bs-toggle="card-collapse"]', function (e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-collapsed');
		e.preventDefault();
		return false;
	});

	// ______________ Card full screen
	$(document).on('click', '[data-bs-toggle="card-fullscreen"]', function (e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-fullscreen').removeClass('card-collapsed');
		e.preventDefault();
		return false;
	});

	// ______________Main-navbar
	if (window.matchMedia('(min-width: 992px)').matches) {
		$('.main-navbar .active').removeClass('show');
		$('.main-header-menu .active').removeClass('show');
	}
	$('.main-header .dropdown > a').on('click', function (e) {
		e.preventDefault();
		$(this).parent().toggleClass('show');
		$(this).parent().siblings().removeClass('show');
	});
	$('.mobile-main-header .dropdown > a').on('click', function (e) {
		e.preventDefault();
		$(this).parent().toggleClass('show');
		$(this).parent().siblings().removeClass('show');
	});
	$('.main-navbar .with-sub').on('click', function (e) {
		e.preventDefault();
		$(this).parent().toggleClass('show');
		$(this).parent().siblings().removeClass('show');
	});
	$('.dropdown-menu .main-header-arrow').on('click', function (e) {
		e.preventDefault();
		$(this).closest('.dropdown').removeClass('show');
	});
	$('#mainSidebarToggle').on('click', function (e) {
		e.preventDefault();
		$('body.horizontalmenu').toggleClass('main-navbar-show');
	});
	$('#mainContentLeftShow').on('click touch', function (e) {
		e.preventDefault();
		$('body').addClass('main-content-left-show');
	});
	$('#mainContentLeftHide').on('click touch', function (e) {
		e.preventDefault();
		$('body').removeClass('main-content-left-show');
	});
	$('#mainContentBodyHide').on('click touch', function (e) {
		e.preventDefault();
		$('body').removeClass('main-content-body-show');
	})
	$('body').append('<div class="main-navbar-backdrop"></div>');
	$('.main-navbar-backdrop').on('click touchstart', function () {
		$('body').removeClass('main-navbar-show');
	});



	// ______________Dropdown menu
	$(document).on('click touchstart', function (e) {
		e.stopPropagation();
		var dropTarg = $(e.target).closest('.main-header .dropdown').length;
		if (!dropTarg) {
			$('.main-header .dropdown').removeClass('show');
		}
		if (window.matchMedia('(min-width: 992px)').matches) {
			var navTarg = $(e.target).closest('.main-navbar .nav-item').length;
			if (!navTarg) {
				$('.main-navbar .show').removeClass('show');
			}
			var menuTarg = $(e.target).closest('.main-header-menu .nav-item').length;
			if (!menuTarg) {
				$('.main-header-menu .show').removeClass('show');
			}
			if ($(e.target).hasClass('main-menu-sub-mega')) {
				$('.main-header-menu .show').removeClass('show');
			}
		} else {
			if (!$(e.target).closest('#mainMenuShow').length) {
				var hm = $(e.target).closest('.main-header-menu').length;
				if (!hm) {
					$('body').removeClass('main-header-menu-show');
				}
			}
		}
	});

	// // ______________MainMenuShow
	$('#mainMenuShow').on('click', function (e) {
		e.preventDefault();
		$('body').toggleClass('main-header-menu-show');
	})
	$('.main-header-menu .with-sub').on('click', function (e) {
		e.preventDefault();
		$(this).parent().toggleClass('show');
		$(this).parent().siblings().removeClass('show');
	})
	$('.main-header-menu-header .close').on('click', function (e) {
		e.preventDefault();
		$('body').removeClass('main-header-menu-show');
	})

	// // ______________Popover
	var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
	var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
		return new bootstrap.Popover(popoverTriggerEl)
	})

	// // ______________Tooltip
	var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
	var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
		return new bootstrap.Tooltip(tooltipTriggerEl)
	})

	// // ______________Toast
	$(".toast").toast();

	// // ______________Live Toast
	var toastTrigger = document.getElementById('liveToastBtn')
	var toastLiveExample = document.getElementById('liveToast')
	if (toastTrigger) {
		toastTrigger.addEventListener('click', function () {
			var toast = new bootstrap.Toast(toastLiveExample)

			toast.show()
		})
	}

	// // ______________Back-top-button
	$(window).on("scroll", function (e) {
		if ($(this).scrollTop() > 0) {
			$('#back-to-top').fadeIn('slow');
		} else {
			$('#back-to-top').fadeOut('slow');
		}
	});
	$(document).on("click", "#back-to-top", function (e) {
		$("html, body").animate({
			scrollTop: 0
		}, 0);
		return false;
	});

	// // ______________Full screen
	$(document).on("click", ".fullscreen-button", function toggleFullScreen() {
		$('html').addClass('fullscreen');
		if ((document.fullScreenElement !== undefined && document.fullScreenElement === null) || (document.msFullscreenElement !== undefined && document.msFullscreenElement === null) || (document.mozFullScreen !== undefined && !document.mozFullScreen) || (document.webkitIsFullScreen !== undefined && !document.webkitIsFullScreen)) {
			if (document.documentElement.requestFullScreen) {
				document.documentElement.requestFullScreen();
			} else if (document.documentElement.mozRequestFullScreen) {
				document.documentElement.mozRequestFullScreen();
			} else if (document.documentElement.webkitRequestFullScreen) {
				document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
			} else if (document.documentElement.msRequestFullscreen) {
				document.documentElement.msRequestFullscreen();
			}
		} else {
			$('html').removeClass('fullscreen');
			if (document.cancelFullScreen) {
				document.cancelFullScreen();
			} else if (document.mozCancelFullScreen) {
				document.mozCancelFullScreen();
			} else if (document.webkitCancelFullScreen) {
				document.webkitCancelFullScreen();
			} else if (document.msExitFullscreen) {
				document.msExitFullscreen();
			}
		}
	})

	// //Input file-browser
	$(document).on('change', '.file-browserinput', function () {
		var input = $(this),
			numFiles = input.get(0).files ? input.get(0).files.length : 1,
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
		input.trigger('fileselect', [numFiles, label]);
	});// We can watch for our custom `fileselect` event like this

	// // ______________Cover Image
	$(".cover-image").each(function () {
		var attr = $(this).attr('data-image-src');
		if (typeof attr !== typeof undefined && attr !== false) {
			$(this).css('background', 'url(' + attr + ') center center');
		}
	});

	// // ______________Accordion Style
	$(document).on("click", '[data-bs-toggle="collapse"]', function () {
		$(this).toggleClass('active').siblings().removeClass('active');
	});

	// // ______________EMAIL INBOX
	$(".clickable-row").on('click', function () {
		window.location = $(this).data("href");
	});

	// // ______________Horizontal-menu Active Class
	function addActiveClass(element) {
		if (current === "") {
			if (element.attr('href').indexOf("#") !== -1) {
				element.parents('.main-navbar .nav-item').last().removeClass('active');
				if (element.parents('.main-navbar .nav-sub').length) {
					element.parents('.main-navbar .nav-sub-item').last().removeClass('active');
				}
			}
		} else {
			if (element.attr('href').indexOf(current) !== -1) {
				element.parents('.main-navbar .nav-item').last().addClass('active');
				if (element.parents('.main-navbar .nav-sub').length) {
					element.parents('.main-navbar .nav-sub-item').last().addClass('active');
				}
			}
		}
	}
	var current = location.pathname.split("/").slice(-1)[0].replace(/^\/|\/$/g, '');
	$('.main-navbar .nav li a').each(function () {
		var $this = $(this);
		addActiveClass($this);
	})


	// /* Headerfixed */
	$(window).on("scroll", function (e) {
		if ($(window).scrollTop() >= 66) {
			$('.main-header').addClass('fixed-header');
		}
		else {
			$('.main-header').removeClass('fixed-header');
		}
	});


	/*Switcher Toggle Start*/
	$('.layout-setting').on("click", function (e) {
		if (document) {
			$('body').toggleClass('dark-theme');
		} else {
			$('body').removeClass('dark-theme');
			$('body').addClass('light-theme');
		}
	});
	/*Switcher Toggle End*/

	$('.layout-setting').on("click", function(e) {
		if (!(document.querySelector('body').classList.contains('dark-theme'))) {
			$('body').addClass('dark-theme');
			$('body').removeClass('light-theme');
			$('body').removeClass('transparent-theme');

            $('#myonoffswitch5').prop('checked', true);
            $('#myonoffswitch8').prop('checked', true);

			localStorage.setItem('darkMode', true);
			localStorage.removeItem('lightMode');
			localStorage.removeItem('transparentMode');
            $('#myonoffswitch2').prop('checked', true);
            
		} 
	});


	// /*Light Theme Start*/
	$(document).on("click", '#myonoffswitch1', function () {
		if (this.checked) {
			$('body').addClass('light-theme');
			localStorage.setItem("dark-menu", "true")
			$('body').removeClass('dark-theme');
			$('body').removeClass('transparent-theme');
			$('body').addClass('dark-menu');
			$('#myonoffswitch3').prop('checked', true);
			$('#myonoffswitch6').prop('checked', true);
			// remove dark theme properties	
			localStorage.removeItem('darkPrimary')

			// remove light theme properties
			localStorage.removeItem('primaryColor')
			localStorage.removeItem('primaryHoverColor')
			localStorage.removeItem('primaryBorderColor')
			document.querySelector('html')?.style.removeProperty('--primary-bg-color', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--primary-bg-hover', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--primary-bg-border', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--dark-primary', localStorage.darkPrimary);

			// removing dark theme properties
			localStorage.removeItem('darkPrimary')
			localStorage.removeItem('transparentBgColor');
			localStorage.removeItem('transparentThemeColor');
			localStorage.removeItem('transparentPrimary');
			localStorage.removeItem('darkprimaryTransparent');
			localStorage.removeItem('transparentBgImgPrimary');
			localStorage.removeItem('transparentBgImgprimaryTransparent');

			$('#myonoffswitch1').prop('checked', true);
			$('#myonoffswitch2').prop('checked', false);
			$('#myonoffswitchTransparent').prop('checked', false);

			checkOptions();
			const root = document.querySelector(':root');
			root.style = "";
			names()
		} 
		localStorageBackup();
	});
	// /*Light Theme End*/

	// /*Dark Theme Start*/
	$(document).on("click", '#myonoffswitch2', function () {
		if (this.checked) {
			$('body').addClass('dark-theme');
			$('body').removeClass('light-theme');
			$('body').removeClass('transparent-theme');
			$('#myonoffswitch5').prop('checked', true);
			$('#myonoffswitch8').prop('checked', true);


			// remove light theme properties
			localStorage.removeItem('primaryColor')
			localStorage.removeItem('primaryHoverColor')
			localStorage.removeItem('primaryBorderColor')
			localStorage.removeItem('darkPrimary')
			document.querySelector('html')?.style.removeProperty('--primary-bg-color', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--primary-bg-hover', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--primary-bg-border', localStorage.darkPrimary);
			document.querySelector('html')?.style.removeProperty('--dark-primary', localStorage.darkPrimary);

			// removing light theme data 
			localStorage.removeItem('primaryColor')
			localStorage.removeItem('primaryHoverColor')
			localStorage.removeItem('primaryBorderColor')
			localStorage.removeItem('primaryTransparent');

			localStorage.removeItem('transparentBgColor');
			localStorage.removeItem('transparentThemeColor');
			localStorage.removeItem('transparentPrimary');
			localStorage.removeItem('transparentBgImgPrimary');
			localStorage.removeItem('transparentBgImgprimaryTransparent');

			$('#myonoffswitch1').prop('checked', false);
			$('#myonoffswitch2').prop('checked', true);
			$('#myonoffswitchTransparent').prop('checked', false);
			checkOptions();

			const root = document.querySelector(':root');
			root.style = "";
			names()
		} 
		localStorageBackup()
	});
	// /*Dark Theme End*/

	// /*Transparent Theme Start*/
	$(document).on("click", '#myonoffswitchTransparent', function () {
		if (this.checked) {
			$('body').addClass('transparent-theme');
			$('body').removeClass('dark-theme');
			$('body').removeClass('light-theme');
			$('body').removeClass('dark-menu');
			$('#myonoffswitch3').prop('checked', false);
			$('#myonoffswitch6').prop('checked', false);
			$('#myonoffswitch5').prop('checked', false);
			$('#myonoffswitch8').prop('checked', false);

			// remove light theme properties
			localStorage.removeItem('primaryColor')
			localStorage.removeItem('primaryHoverColor')
			localStorage.removeItem('primaryBorderColor')

			// removing light theme data 
			localStorage.removeItem('darkPrimary');
			localStorage.removeItem('primaryColor')
			localStorage.removeItem('primaryHoverColor')
			localStorage.removeItem('primaryBorderColor')
			localStorage.removeItem('primaryTransparent');
			localStorage.removeItem('transparentPrimary');
			localStorage.removeItem('darkprimaryTransparent');
			localStorage.removeItem('transparentBgImgPrimary');
			localStorage.removeItem('transparentBgImgprimaryTransparent');

			$('#myonoffswitch2').prop('checked', false);
			$('#myonoffswitch1').prop('checked', false);
			$('#myonoffswitchTransparent').prop('checked', true);
			checkOptions();

			localStorage.setItem("dark-menu", "false")
			const root = document.querySelector(':root');
			root.style = "";
			names()
		} 
		localStorageBackup()
		$('body').removeClass('bg-img1');
		$('body').removeClass('bg-img2');
		$('body').removeClass('bg-img3');
		$('body').removeClass('bg-img4');
	});
	// /*Transparent Theme End*/

	/*Transparent Bg-Image Style Start*/
	$(document).on("click", '#bgimage1', function () {
		$('body').addClass('bg-img1');
		$('body').removeClass('bg-img2');
		$('body').removeClass('bg-img3');
		$('body').removeClass('bg-img4');

		document.querySelector('body').classList.add('transparent-theme');
		document.querySelector('body')?.classList.remove('light-theme');
		document.querySelector('body')?.classList.remove('dark-theme');

		$('#myonoffswitch2').prop('checked', false);
		$('#myonoffswitch1').prop('checked', false);
		$('#myonoffswitchTransparent').prop('checked', true);

		checkOptions();
		
	localStorage.setItem("dark-menu", "false")
	})

	$(document).on("click", '#bgimage2', function () {
		$('body').addClass('bg-img2');
		$('body').removeClass('bg-img1');
		$('body').removeClass('bg-img3');
		$('body').removeClass('bg-img4');

		document.querySelector('body').classList.add('transparent-theme');
		document.querySelector('body')?.classList.remove('light-theme');
		document.querySelector('body')?.classList.remove('dark-theme');

		$('#myonoffswitch2').prop('checked', false);
		$('#myonoffswitch1').prop('checked', false);
		$('#myonoffswitchTransparent').prop('checked', true);

		checkOptions();
		localStorage.setItem("dark-menu", "false")
	})

	$(document).on("click", '#bgimage3', function () {
		$('body').addClass('bg-img3');
		$('body').removeClass('bg-img1');
		$('body').removeClass('bg-img2');
		$('body').removeClass('bg-img4');

		document.querySelector('body').classList.add('transparent-theme');
		document.querySelector('body')?.classList.remove('light-theme');
		document.querySelector('body')?.classList.remove('dark-theme');

		$('#myonoffswitch2').prop('checked', false);
		$('#myonoffswitch1').prop('checked', false);
		$('#myonoffswitchTransparent').prop('checked', true);

		checkOptions();
		
	localStorage.setItem("dark-menu", "false")
	})

	$(document).on("click", '#bgimage4', function () {
		$('body').addClass('bg-img4');
		$('body').removeClass('bg-img1');
		$('body').removeClass('bg-img2');
		$('body').removeClass('bg-img3');

		document.querySelector('body').classList.add('transparent-theme');
		document.querySelector('body')?.classList.remove('light-theme');
		document.querySelector('body')?.classList.remove('dark-theme');
		$('#myonoffswitch2').prop('checked', false);
		$('#myonoffswitch1').prop('checked', false);
		$('#myonoffswitchTransparent').prop('checked', true);

		checkOptions();
		localStorage.setItem("dark-menu", "false")
	})
	// /*Transparent Bg-Image Style End*/

	// /*Light Menu Start*/
	$(document).on("click", '#myonoffswitch3', function () {
		if (this.checked) {
			$('body').addClass('light-menu');
			$('body').removeClass('color-menu');
			$('body').removeClass('dark-menu');
		} 
	});
	// /*Light Menu End*/

	// /*Color Menu Start*/
	$(document).on("click", '#myonoffswitch4', function () {
		if (this.checked) {
			$('body').addClass('color-menu');
			$('body').removeClass('light-menu');
			$('body').removeClass('dark-menu');
		} 
	});
	// /*Color Menu End*/

	// /*Dark Menu Start*/
	$(document).on("click", '#myonoffswitch5', function () {
		if (this.checked) {
			$('body').addClass('dark-menu');
			$('body').removeClass('color-menu');
			$('body').removeClass('light-menu');
		}
	});
	// /*Dark Menu End*/

	// /*Light Header Start*/
	$(document).on("click", '#myonoffswitch6', function () {
		if (this.checked) {
			$('body').addClass('header-light');
			$('body').removeClass('color-header');
			$('body').removeClass('header-dark');
		} 
	});
	// /*Light Header End*/

	// /*Color Header Start*/
	$(document).on("click", '#myonoffswitch7', function () {
		if (this.checked) {
			$('body').addClass('color-header');
			$('body').removeClass('header-light');
			$('body').removeClass('header-dark');
		} 
	});
	// /*Color Header End*/

	// /*Dark Header Start*/
	$(document).on("click", '#myonoffswitch8', function () {
		if (this.checked) {
			$('body').addClass('header-dark');
			$('body').removeClass('color-header');
			$('body').removeClass('header-light');
		} 
	});
	// /*Dark Header End*/

	// /*Full Width Layout Start*/
	$(document).on("click", '#myonoffswitch9', function () {
		if (this.checked) {
			$('body').addClass('layout-fullwidth');
			$('body').removeClass('layout-boxed');
		}
	});
	// /*Full Width Layout End*/

	// /*Boxed Layout Start*/
	$(document).on("click", '#myonoffswitch10', function () {
		if (this.checked) {
			$('body').addClass('layout-boxed');
			$('body').removeClass('layout-fullwidth');
		} 
	});
	// /*Boxed Layout End*/

	// /*Header-Position Styles Start*/
	$(document).on("click", '#myonoffswitch11', function () {
		if (this.checked) {
			$('body').addClass('fixed-layout');
			$('body').removeClass('scrollable-layout');
		} 
	});
	$(document).on("click", '#myonoffswitch12', function () {
		if (this.checked) {
			$('body').addClass('scrollable-layout');
			$('body').removeClass('fixed-layout');
		}
	});
	// /*Header-Position Styles End*/

	// /*Default Sidemenu Start*/
	$(document).on("click", '#myonoffswitch13', function () {
		if (this.checked) {
			$('body').addClass('default-menu');
			$('body').removeClass('main-sidebar-hide');
			hovermenu();
			$('body').removeClass('icontext-menu');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('hover-submenu1');
		} 
	});
	// /*Default Sidemenu End*/

	// /*Icon Text Sidemenu Start*/
	$(document).on("click", '#myonoffswitch14', function () {
		if (this.checked) {
			$('body').addClass('icontext-menu');
			icontext();
			$('body').addClass('main-sidebar-hide');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('hover-submenu1');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('hover-submenu');
		} 
	});
	// /*Icon Text Sidemenu End*/

	// /*Icon Overlay Sidemenu Start*/
	$(document).on("click", '#myonoffswitch15', function () {
		if (this.checked) {
			$('body').addClass('icon-overlay');
			hovermenu();
			$('body').addClass('main-sidebar-hide');
			$('body').removeClass('hover-submenu1');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('icontext-menu');
		} 
	});
	// /*Icon Overlay Sidemenu End*/

	/*Closed Sidemenu Start*/
	$(document).on("click", '#myonoffswitch16', function () {
		if (this.checked) {
			$('body').addClass('closed-leftmenu');
			$('body').addClass('main-sidebar-hide');
			$('body').removeClass('default-menu');
			$('body').removeClass('hover-submenu1');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('icontext-menu');

		} 
	});
	/*Closed Sidemenu End*/

	/*Hover Submenu Start*/
	$(document).on("click", '#myonoffswitch17', function () {
		if (this.checked) {
			$('body').addClass('hover-submenu');
			hovermenu();
			$('body').addClass('main-sidebar-hide');
			$('body').removeClass('hover-submenu1');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('icontext-menu');
		} 
	});
	/*Hover Submenu End*/

	/*Hover Submenu Style 1 Start*/
	$(document).on("click", '#myonoffswitch18', function () {
		if (this.checked) {
			$('body').addClass('hover-submenu1');
			hovermenu();
			$('body').addClass('main-sidebar-hide');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('icontext-menu');
		} 
	});
	/*Hover Submenu Style 1 End*/

	/* Vertical Menu Start */
	$(document).on("click", '#myonoffswitch01', function () {
		if (this.checked) {
			$('body').addClass('leftmenu');
			$('body').addClass('main-body');
			$('body').removeClass('horizontalmenu');
			$('body').removeClass('horizontalmenu-hover');
			$('.main-content').addClass('side-content');
			$('.main-header').removeClass(' hor-header');
			$('.main-header').addClass('sticky');
			$('.main-content').removeClass('hor-content');
			$('.main-container').removeClass('container');
			$('.main-container-1').removeClass('container');
			$('.main-container').addClass('container-fluid');
			$('.main-menu').removeClass('main-navbar hor-menu ');
			$('.main-menu').addClass('main-sidebar main-sidebar-sticky side-menu');
			$('.main-container-1').addClass('main-sidebar-header');
			$('.main-body-1').addClass('main-sidebar-body');
			$('.menu-icon').addClass('sidemenu-icon');
			$('.menu-icon').removeClass('hor-icon');
			HorizontalHovermenu();
		} 
	});
	/* Vertical Menu End */

	/* Horizontal Menu Start */
	$(document).on("click", '#myonoffswitch02', function () {
		if (this.checked) {
			checkHoriMenu();
			$('body').addClass('horizontalmenu');
			$('body').removeClass('horizontalmenu-hover');
			$('body').removeClass('leftmenu');
			$('body').removeClass('main-body');
			$('.main-content').addClass('hor-content');
			$('.main-header').addClass('hor-header');
			$('.main-header').removeClass('sticky');
			$('.main-content').removeClass('side-content');
			$('.main-container').addClass('container');
			$('.main-container-1').addClass('container');
			$('.main-container').removeClass('container-fluid');
			$('.main-menu').addClass('main-navbar hor-menu');
			$('.main-menu').removeClass('main-sidebar main-sidebar-sticky side-menu');
			$('.main-container-1').removeClass('main-sidebar-header');
			$('.main-body-1').removeClass('main-sidebar-body');
			$('.menu-icon').removeClass('sidemenu-icon');
			$('.menu-icon').addClass('hor-icon');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('icontext-menu');
			$('body').removeClass('main-sidebar-hide');
			$('body').removeClass('main-sidebar-open');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('hover-submenu1');
			HorizontalHovermenu();
		} 
	});
	/*Horizontal Menu End */

	/* Horizontal Hover Menu Start */
	$(document).on("click", '#myonoffswitch03', function () {
		if (this.checked) {
			let subNavSub = document.querySelectorAll('.sub-nav-sub');
			subNavSub.forEach((e) => {
				e.style.display = '';
			})
			let subNav = document.querySelectorAll('.nav-sub')
			subNav.forEach((e) => {
				e.style.display = '';
			})
			checkHoriMenu();
			$('body').addClass('horizontalmenu');
			$('body').addClass('horizontalmenu-hover');
			$('body').removeClass('leftmenu');
			$('body').removeClass('main-body');
			$('.main-content').addClass('hor-content');
			$('.main-header').addClass('hor-header');
			$('.main-header').removeClass('sticky');
			$('.main-content').removeClass('side-content');
			$('.main-container').addClass('container');
			$('.main-container-1').addClass('container');
			$('.main-container').removeClass('container-fluid');
			$('.main-menu').addClass('main-navbar hor-menu');
			$('.main-menu').removeClass('main-sidebar main-sidebar-sticky side-menu');
			$('.main-container-1').removeClass('main-sidebar-header');
			$('.main-body-1').removeClass('main-sidebar-body');
			$('.menu-icon').removeClass('sidemenu-icon');
			$('.menu-icon').addClass('hor-icon');
			$('body').removeClass('default-menu');
			$('body').removeClass('closed-leftmenu');
			$('body').removeClass('icontext-menu');
			$('body').removeClass('main-sidebar-hide');
			$('body').removeClass('main-sidebar-open');
			$('body').removeClass('icon-overlay');
			$('body').removeClass('hover-submenu');
			$('body').removeClass('hover-submenu1');
			HorizontalHovermenu();
		} else {
			$('body').removeClass('horizontalmenu');
			$('body').removeClass('horizontalmenu-hover');
			$('body').addClass('leftmenu');
		}
	});
	/* Horizontal Hover Menu End */


	//On ready function for Horizontal Menu
	    
	
		function light(){
			if(localStorage.getItem("dark-menu") == null || localStorage.getItem("dark-menu") == undefined){
				localStorage.setItem("dark-menu", "true")
			}
			
			if(document.querySelector('body').classList.contains('light-theme')){
				$('#myonoffswitch5').prop('checked', true);
				$('#myonoffswitch6').prop('checked', true);
			}
			
			if(localStorage.getItem("dark-menu") == 'true'){
				document.querySelector('body')?.classList.add('dark-menu')
			}
			else{
				document.querySelector('body')?.classList.remove('dark-menu')
			}
		}
		light();



	// /* LTR version Start */
	$(document).on("click", '#myonoffswitch19', function () {
		if (this.checked) {
			$('body').addClass('ltr');
			if(document.querySelector('body .page').classList.contains('main-signin-wrapper') != true){
				checkHoriMenu();
			}
			$('body').removeClass('rtl');
			$("html[lang=en]").attr("dir", "ltr");
			localStorage.setItem("ltr", "True");
			$("head link#style").attr("href", $(this));
			(document.getElementById("style").setAttribute("href", "static/assets/plugins/bootstrap/css/bootstrap.min.css"));
			var carousel = $('.owl-carousel');
			$.each(carousel, function (index, element) {
				// element == this
				var carouselData = $(element).data('owl.carousel');
				carouselData.settings.rtl = false; //don't know if both are necessary
				carouselData.options.rtl = false;
				$(element).trigger('refresh.owl.carousel');
			});

		}
		
	});
	// /* LTR version End */


	// /* RTL version Start */
	$(document).on("click", '#myonoffswitch20', function () {
		if (this.checked) {
			$('body').addClass('rtl');
			if(document.querySelector('body .page').classList.contains('main-signin-wrapper') != true){
				checkHoriMenu();
			}
			$('body').removeClass('ltr');
			$("html[lang=en]").attr("dir", "rtl");
			localStorage.setItem("rtl", "True");
			$("head link#style").attr("href", $(this));
			(document.getElementById("style").setAttribute("href", "static/assets/plugins/bootstrap/css/bootstrap.rtl.min.css"));
			var carousel = $('.owl-carousel');
			$.each(carousel, function (index, element) {
				// element == this
				var carouselData = $(element).data('owl.carousel');
				carouselData.settings.rtl = true; //don't know if both are necessary
				carouselData.options.rtl = true;
				$(element).trigger('refresh.owl.carousel');
			});
		}
	});
	// /* RTL version End */

	});

function checkOptions() {
	// light header 
	if (document.querySelector('body').classList.contains('header-light')) {
		$('#myonoffswitch6').prop('checked', true);
	}
	// color header 
	if (document.querySelector('body').classList.contains('color-header')) {
		$('#myonoffswitch7').prop('checked', true);
	}
	// dark header 
	if (document.querySelector('body').classList.contains('header-dark')) {
		$('#myonoffswitch8').prop('checked', true);
	}

	// light menu
	if (document.querySelector('body').classList.contains('light-menu')) {
		$('#myonoffswitch3').prop('checked', true);
	}
	// color menu
	if (document.querySelector('body').classList.contains('color-menu')) {
		$('#myonoffswitch4').prop('checked', true);
	}
	// dark menu
	if (document.querySelector('body').classList.contains('dark-menu')) {
		$('#myonoffswitch5').prop('checked', true);
	}
}
$(function () {
	'use strict'

	let bodyRtl = $('body').hasClass('rtl');
	if (bodyRtl) {
		$('body').addClass('rtl');
		$("html[lang=en]").attr("dir", "rtl");
		$("head link#style").attr("href", $(this));
		(document.getElementById("style")?.setAttribute("href", "static/assets/plugins/bootstrap/css/bootstrap.rtl.min.css"));

		var carousel = $('.owl-carousel');
		$.each(carousel, function (index, element) {
			// element == this
			var carouselData = $(element).data('owl.carousel');
			carouselData.settings.rtl = true; //don't know if both are necessary
			carouselData.options.rtl = true;
			$(element).trigger('refresh.owl.carousel');
		});
	}


	let bodyhorizontalhover = $('body').hasClass('horizontalmenu-hover');
	if (bodyhorizontalhover) {
		$('body').addClass('horizontalmenu');
		$('body').addClass('horizontalmenu-hover');
		$('body').removeClass('leftmenu');
		$('body').removeClass('main-body');
		$('.main-content').addClass('hor-content');
		$('.main-header').addClass(' hor-header');
		$('.main-header').removeClass('sticky');
		$('.main-content').removeClass('side-content');
		$('.main-container').addClass('container');
		$('.main-container-1').addClass('container');
		$('.main-container').removeClass('container-fluid');
		$('.main-menu').addClass('main-navbar hor-menu');
		$('.main-menu').removeClass('main-sidebar main-sidebar-sticky side-menu');
		$('.main-container-1').removeClass('main-sidebar-header');
		$('.main-body-1').removeClass('main-sidebar-body');
		$('.menu-icon').removeClass('sidemenu-icon');
		$('.menu-icon').addClass('hor-icon');
		$('body').removeClass('default-menu');
		$('body').removeClass('closed-leftmenu');
		$('body').removeClass('icontext-menu');
		$('body').removeClass('main-sidebar-hide');
		$('body').removeClass('main-sidebar-open');
		$('body').removeClass('icon-overlay');
		$('body').removeClass('hover-submenu');
		$('body').removeClass('hover-submenu1');
	}
	let bodyhorizontal = $('body').hasClass('horizontalmenu');
	if (bodyhorizontal) {
		$('body').addClass('horizontalmenu');
		$('body').removeClass('leftmenu');
		$('body').removeClass('main-body');
		$('.main-content').addClass('hor-content');
		$('.main-header').addClass(' hor-header');
		$('.main-header').removeClass('sticky');
		$('.main-content').removeClass('side-content');
		$('.main-container').addClass('container');
		$('.main-container-1').addClass('container');
		$('.main-container').removeClass('container-fluid');
		$('.main-menu').addClass('main-navbar hor-menu');
		$('.main-menu').removeClass('main-sidebar main-sidebar-sticky side-menu');
		$('.main-container-1').removeClass('main-sidebar-header');
		$('.main-body-1').removeClass('main-sidebar-body');
		$('.menu-icon').removeClass('sidemenu-icon');
		$('.menu-icon').addClass('hor-icon');
		$('body').removeClass('default-menu');
		$('body').removeClass('closed-leftmenu');
		$('body').removeClass('icontext-menu');
		$('body').removeClass('main-sidebar-hide');
		$('body').removeClass('main-sidebar-open');
		$('body').removeClass('icon-overlay');
		$('body').removeClass('hover-submenu');
		$('body').removeClass('hover-submenu1');
	}
})