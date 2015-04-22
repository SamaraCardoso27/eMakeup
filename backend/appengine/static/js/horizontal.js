jQuery(function($){'use strict';(function(){var $frame=$('#basic');var $slidee=$frame.children('ul').eq(0);var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'basic',smart:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:3,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,pagesBar:$wrap.find('.pages'),activatePageOn:'click',speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,forward:$wrap.find('.forward'),backward:$wrap.find('.backward'),prev:$wrap.find('.prev'),next:$wrap.find('.next'),prevPage:$wrap.find('.prevPage'),nextPage:$wrap.find('.nextPage')});$wrap.find('.toStart').on('click',function(){var item=$(this).data('item');$frame.sly('toStart',item);});$wrap.find('.toCenter').on('click',function(){var item=$(this).data('item');$frame.sly('toCenter',item);});$wrap.find('.toEnd').on('click',function(){var item=$(this).data('item');$frame.sly('toEnd',item);});$wrap.find('.add').on('click',function(){$frame.sly('add','<li>'+ $slidee.children().length+'</li>');});$wrap.find('.remove').on('click',function(){$frame.sly('remove',-1);});}());(function(){var $frame=$('#centered');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'centered',smart:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:7,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,prev:$wrap.find('.prev'),next:$wrap.find('.next')});}());(function(){var $frame=$('#forcecentered');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'forceCentered',smart:1,activateMiddle:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:0,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,prev:$wrap.find('.prev'),next:$wrap.find('.next')});}());(function(){var $frame=$('#cycleitems');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'basic',smart:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:0,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,cycleBy:'items',cycleInterval:1000,pauseOnHover:1,prev:$wrap.find('.prev'),next:$wrap.find('.next')});$wrap.find('.pause').on('click',function(){$frame.sly('pause');});$wrap.find('.resume').on('click',function(){$frame.sly('resume');});$wrap.find('.toggle').on('click',function(){$frame.sly('toggle');});}());(function(){var $frame=$('#cyclepages');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'basic',smart:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:0,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,pagesBar:$wrap.find('.pages'),activatePageOn:'click',speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,cycleBy:'pages',cycleInterval:1000,pauseOnHover:1,startPaused:1,prevPage:$wrap.find('.prevPage'),nextPage:$wrap.find('.nextPage')});$wrap.find('.pause').on('click',function(){$frame.sly('pause');});$wrap.find('.resume').on('click',function(){$frame.sly('resume');});$wrap.find('.toggle').on('click',function(){$frame.sly('toggle');});}());(function(){var $frame=$('#oneperframe');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'forceCentered',smart:1,activateMiddle:1,mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:0,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,prev:$wrap.find('.prev'),next:$wrap.find('.next')});}());(function(){var $frame=$('#effects');var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'forceCentered',smart:1,activateMiddle:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:3,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,speed:300,elasticBounds:1,easing:'swing',dragHandle:1,dynamicHandle:1,clickBar:1,prev:$wrap.find('.prev'),next:$wrap.find('.next')});}());(function(){var $frame=$('#crazy');var $slidee=$frame.children('ul').eq(0);var $wrap=$frame.parent();$frame.sly({horizontal:1,itemNav:'basic',smart:1,activateOn:'click',mouseDragging:1,touchDragging:1,releaseSwing:1,startAt:3,scrollBar:$wrap.find('.scrollbar'),scrollBy:1,pagesBar:$wrap.find('.pages'),activatePageOn:'click',speed:300,elasticBounds:1,easing:'easeOutExpo',dragHandle:1,dynamicHandle:1,clickBar:1,forward:$wrap.find('.forward'),backward:$wrap.find('.backward'),prev:$wrap.find('.prev'),next:$wrap.find('.next'),prevPage:$wrap.find('.prevPage'),nextPage:$wrap.find('.nextPage')});$wrap.find('.toStart').on('click',function(){var item=$(this).data('item');$frame.sly('toStart',item);});$wrap.find('.toCenter').on('click',function(){var item=$(this).data('item');$frame.sly('toCenter',item);});$wrap.find('.toEnd').on('click',function(){var item=$(this).data('item');$frame.sly('toEnd',item);});$wrap.find('.add').on('click',function(){$frame.sly('add','<li>'+ $slidee.children().length+'</li>');});$wrap.find('.remove').on('click',function(){$frame.sly('remove',-1);});}());});