import services_animation_both from "./services_animation_both";
import xp_animation_desktop from "./xp_animation_desktop";
import certificates_animation_both from "./certificates_animation_both";
import xp_animation_mobile from "./xp_animation_mobile";
import blog_animation_landing from "../../blog/blog_animation_landing";

gsap.registerPlugin(ScrollTrigger);
document.addEventListener('DOMContentLoaded', () => {
    ScrollTrigger.matchMedia({
        "(max-width: 750px)" : function() {
            services_animation_both();
            certificates_animation_both();
            xp_animation_mobile();
            blog_animation_landing();
        },
        "(min-width: 751px)" : function() {
            services_animation_both();
            certificates_animation_both();
            xp_animation_desktop();
            blog_animation_landing();
        }
    });
});
