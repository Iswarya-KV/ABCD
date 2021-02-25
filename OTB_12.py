# Since the access to the ABCD data has not been obtained, this exercise can also be done so
# Make a custom palette with gendered colors
# Note: this is equivalent to {"M": "#6495ED", "F": "#F08080"}
pal = dict(M="#6495ED", F="#F08080")

# Show the survival probability as a function of age and sex
g = sns.lmplot(x='pps_y_ss_severity_score', y='smri_vol_cdk_total', col="sex", hue="sex", data=subset_df,
               palette=pal, y_jitter=.02, logistic=False, truncate=False)


# Scatterplot
sns.pairplot(subset_df, hue="sex", vars=["anthroweightcalc", 'ksads_1_2_t', 'prosocial_q2_y', "smri_vol_scs_amygdalalh"]);
# or

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


# Multiple interactive plots
# Create an interactive parallel coordinate plot
subset_df_numerical = subset_df.copy()
subset_df_numerical.sex = subset_df.sex.astype("category").cat.codes
subset_df_numerical.site_id_l = subset_df.site_id_l.astype("category").cat.codes
fig = px.parallel_coordinates(subset_df_numerical, color="interview_age", 
                              dimensions=["interview_age", "sex"] + data_elements_of_interest,
                              color_continuous_scale=px.colors.sequential.Agsunset,)
                              #color_continuous_midpoint=2)
fig.show()


