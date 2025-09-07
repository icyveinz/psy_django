import blog_animation_landing from "./blog_animation_landing";
import blog_animation_static from "./blog_animation_static";

gsap.registerPlugin(ScrollTrigger);
document.addEventListener('DOMContentLoaded', () => {
    ScrollTrigger.matchMedia({
        "(max-width: 750px)" : function() {
            blog_animation_landing();
        },
        "(min-width: 751px)" : function() {
            blog_animation_static();
        }
    });
});