import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

print "Number of jobs under consideration"
num_jobs = int(raw_input())
scores = []
x_sal = np.arange(0, 11, 1)
x_int = np.arange(0, 11, 1)
x_dist  = np.arange(0, 11, 1)
x_score = np.arange(0, 11, 1)

# Generate fuzzy membership functions
sal_lo = fuzz.trimf(x_sal, [0, 0, 5])
sal_md = fuzz.trimf(x_sal, [0, 5, 10])
sal_hi = fuzz.trimf(x_sal, [5, 10, 10])
int_lo = fuzz.trimf(x_int, [0, 0, 5])
int_md = fuzz.trimf(x_int, [0, 5, 10])
int_hi = fuzz.trimf(x_int, [5, 10, 10])
dist_lo = fuzz.trimf(x_dist, [0, 0, 5])
dist_md = fuzz.trimf(x_dist, [0, 5, 10])
dist_hi = fuzz.trimf(x_dist, [5, 10, 10])
score_lo = fuzz.trimf(x_score, [0, 0, 5])
score_md = fuzz.trimf(x_score, [0, 5, 10])
score_hi = fuzz.trimf(x_score, [5, 10, 10])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(x_sal, sal_lo, 'b', linewidth=1.5, label='Low')
ax0.plot(x_sal, sal_md, 'g', linewidth=1.5, label='Medium')
ax0.plot(x_sal, sal_hi, 'r', linewidth=1.5, label='High')
ax0.set_title('Salary')
ax0.legend()

ax1.plot(x_int, int_lo, 'b', linewidth=1.5, label='Low')
ax1.plot(x_int, int_md, 'g', linewidth=1.5, label='Medium')
ax1.plot(x_int, int_hi, 'r', linewidth=1.5, label='High')
ax1.set_title('Interest')
ax1.legend()

ax2.plot(x_dist, dist_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_dist, dist_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_dist, dist_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('Distance')
ax2.legend()

ax3.plot(x_score, score_lo, 'b', linewidth=1.5, label='Low')
ax3.plot(x_score, score_md, 'g', linewidth=1.5, label='Medium')
ax3.plot(x_score, score_hi, 'r', linewidth=1.5, label='High')
ax3.set_title('Score')
ax3.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2, ax3):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

for i in range(num_jobs):
	print "Job " + str(i+1)
	print "On a scale of 0 to 10, how good is the salary?"
	sal = float(raw_input())
	sal_level_lo = fuzz.interp_membership(x_sal, sal_lo, sal)
	sal_level_md = fuzz.interp_membership(x_sal, sal_md, sal)
	sal_level_hi = fuzz.interp_membership(x_sal, sal_hi, sal)

	print "On a scale of 0 to 10, how interesting is the job?"
	inter = float(raw_input())
	int_level_lo = fuzz.interp_membership(x_int, int_lo, inter)
	int_level_md = fuzz.interp_membership(x_int, int_md, inter)
	int_level_hi = fuzz.interp_membership(x_int, int_hi, inter)

	print "On a scale of 0 to 10 (10 being nearest), how close is the workplace?"
	dist = float(raw_input())
	dist_level_lo = fuzz.interp_membership(x_dist, dist_lo, dist)
	dist_level_md = fuzz.interp_membership(x_dist, dist_md, dist)
	dist_level_hi = fuzz.interp_membership(x_dist, dist_hi, dist)

	part1 = min(sal_level_hi, min(int_level_hi,dist_level_hi))
	part2 = min(sal_level_hi, min(int_level_hi,dist_level_md))
	part3 = min(sal_level_hi, min(int_level_hi,dist_level_lo))
	part4 = min(sal_level_md, min(int_level_hi,dist_level_hi))
	part5 = min(sal_level_md, min(int_level_hi,dist_level_md))
	part6 = min(sal_level_lo, min(int_level_hi,dist_level_hi))

	active_rule1 = max(part1,part2,part3,part4,part5,part6)
	score_activation_hi = np.fmin(active_rule1, score_hi)

	part1 = min(sal_level_lo, min(int_level_hi,dist_level_md))
	part2 = min(sal_level_md, min(int_level_md,dist_level_hi))
	part3 = min(sal_level_hi, min(int_level_md,dist_level_hi))
	part4 = min(sal_level_hi, min(int_level_md,dist_level_md))
	part5 = min(sal_level_hi, min(int_level_lo,dist_level_hi))
	part6 = min(sal_level_md, min(int_level_hi,dist_level_lo))
	part7 = min(sal_level_md, min(int_level_md,dist_level_md))
	part8 = min(sal_level_md, min(int_level_md,dist_level_lo))
	part9 = min(sal_level_lo, min(int_level_hi,dist_level_lo))

	active_rule2 = max(part1,part2,part3,part4,part5,part6,part7,part8,part9)
	score_activation_md = np.fmin(active_rule2, score_md)

	# low salary AND low interest AND far
	part1 = min(sal_level_lo, min(int_level_lo,dist_level_lo))
	part2 = min(sal_level_hi, min(int_level_md,dist_level_lo))
	part3 = min(sal_level_hi, min(int_level_lo,dist_level_md))
	part4 = min(sal_level_hi, min(int_level_lo,dist_level_lo)) 
	part5 = min(sal_level_md, min(int_level_lo,dist_level_hi))
	part6 = min(sal_level_md, min(int_level_lo,dist_level_md))
	part7 = min(sal_level_md, min(int_level_lo,dist_level_lo))
	part8 = min(sal_level_lo, min(int_level_md,dist_level_hi))
	part9 = min(sal_level_lo, min(int_level_md,dist_level_md))
	part10 = min(sal_level_lo, min(int_level_md,dist_level_lo))
	part11 = min(sal_level_lo, min(int_level_lo,dist_level_hi))
	part12 = min(sal_level_lo, min(int_level_lo,dist_level_md))

	active_rule3 = max(part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,part11,part12)
	score_activation_lo = np.fmin(active_rule3, score_lo)
	
	score0 = np.zeros_like(x_score)

	# Visualize this
	fig, ax0 = plt.subplots(figsize=(8, 3))

	ax0.fill_between(x_score, score0, score_activation_lo, facecolor='b', alpha=0.7)
	ax0.plot(x_score, score_lo, 'b', linewidth=0.5, linestyle='--', )
	ax0.fill_between(x_score, score0, score_activation_md, facecolor='g', alpha=0.7)
	ax0.plot(x_score, score_md, 'g', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_score, score0, score_activation_hi, facecolor='r', alpha=0.7)
	ax0.plot(x_score, score_hi, 'r', linewidth=0.5, linestyle='--')
	ax0.set_title('Output membership activity')

	# Turn off top/right axes
	for ax in (ax0,):
	    ax.spines['top'].set_visible(False)
	    ax.spines['right'].set_visible(False)
	    ax.get_xaxis().tick_bottom()
	    ax.get_yaxis().tick_left()

	plt.tight_layout()
	plt.show()

	# Aggregate all three output membership functions together
	aggregated = np.fmax(score_activation_lo,
	                     np.fmax(score_activation_md, score_activation_hi))

	# Calculate defuzzified result
	score = fuzz.defuzz(x_score, aggregated, 'centroid')
	scores.append(score)
	score_activation = fuzz.interp_membership(x_score, aggregated, score)  # for plot

	# Visualize this
	fig, ax0 = plt.subplots(figsize=(8, 3))

	ax0.plot(x_score, score_lo, 'b', linewidth=0.5, linestyle='--', )
	ax0.plot(x_score, score_md, 'g', linewidth=0.5, linestyle='--')
	ax0.plot(x_score, score_hi, 'r', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_score, score0, aggregated, facecolor='Orange', alpha=0.7)
	ax0.plot([score, score], [0, score_activation], 'k', linewidth=1.5, alpha=0.9)
	ax0.set_title('Aggregated membership and result (line)')

	# Turn off top/right axes
	for ax in (ax0,):
	    ax.spines['top'].set_visible(False)
	    ax.spines['right'].set_visible(False)
	    ax.get_xaxis().tick_bottom()
	    ax.get_yaxis().tick_left()

	plt.tight_layout()
	plt.show()
print scores