import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The original grid we want to restore
original_grid = '<div class="why-grid"><a href="tailored-solutions.html" class="why-card-link"><article class="why-card"><img src="icon_tailored_solutions.jpg" alt="Tailored Solutions"><h3>Experience tailored Solutions</h3><p>Crafted to fit your unique business needs.</p></article></a><a href="experience-excellence.html" class="why-card-link"><article class="why-card"><img src="icon_excellence.jpg" alt="Excellence"><h3>Experience Excellence</h3><p>Unlock unparalleled excellence as we redefine your journey with our expertise.</p></article></a><a href="timely-customer-service.html" class="why-card-link"><article class="why-card"><img src="icon_customer_service.jpg" alt="Customer Service"><h3>Timely Customer Service</h3><p>Experience peace of mind with our timely service available to assist you.</p></article></a><a href="improve-business.html" class="why-card-link"><article class="why-card"><img class="card-check" src="icon_improve_business.jpg" alt="Improve Business"><h3>Improve your Business</h3><p>Transform your business idea into tailormade solutions to accelerate growth and efficiency.</p></article></a><a href="research-strategy.html" class="why-card-link"><article class="why-card"><img src="icon_research_strategy.jpg" alt="Research and Strategy"><h3>Research And Strategy</h3><p>Elevate your business through meticulous analytics and strategic planning that guides you towards sustainable success.</p></article></a><a href="cutting-edge-solutions.html" class="why-card-link"><article class="why-card"><img src="icon_cutting_edge.jpg" alt="Cutting Edge Solutions"><h3>Cutting Edge Solutions</h3><p>Empower your business with cutting-edge solutions, driving innovation and staying ahead of the curve.</p></article></a></div>'

# Find the start of the coverflow section
start_idx = html.find('<div class="swiper why-coverflow-swiper"')
if start_idx != -1:
    # Find the end of the swiper section (right before </section>)
    end_idx = html.find('</div></section>', start_idx)
    
    if end_idx != -1:
        # We need to include the final </div> that closes the swiper
        end_idx += 6 # length of '</div>'
        
        # Replace the entire swiper block with the original grid
        html = html[:start_idx] + original_grid + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored original why-grid!")
