from project import db
from project.models import Section, Recommendation

# I'm not sure why, but for this app I had to use db.create_all(). See https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/#creating-and-dropping-tables
db.create_all()

Section.query.delete()
Recommendation.query.delete()


sectionA = Section("A", "AML/CFT POLICIES AND COORDINATION")

sectionB = Section("B", "MONEY LAUNDERING AND CONFISCATION")

sectionC = Section("C", "TERRORIST FINANCING AND FINANCING OF PROLIFERATION")

sectionD = Section("D", "PREVENTIVE MEASURES")

sectionE = Section("E", "TRANSPARENCY AND BENEFICIAL OWNERSHIP OF LEGAL PERSONS AND ARRANGEMENTS")

sectionF = Section("F", "POWERS AND RESPONSIBILITIES OF COMPETENT AUTHORITIES AND OTHER INSTITUTIONAL MEASURES")

sectionG = Section("G", "INTERNATIONAL COOPERATION")

db.session.add(sectionA)
db.session.add(sectionB)
db.session.add(sectionC)
db.session.add(sectionD)
db.session.add(sectionE)
db.session.add(sectionF)
db.session.add(sectionG)

db.session.commit()


recommendation1 = Recommendation(
    title="Assessing risks and applying a risk-based approach",
    text="Countries should identify, assess, and understand the money laundering and terrorist financing risks for the country, and should take action, including designating an authority or mechanism to coordinate actions to assess risks, and apply resources, aimed at ensuring the risks are mitigated effectively. Based on that assessment, countries should apply a risk-based approach (RBA) to ensure that measures to prevent or mitigate money laundering and terrorist financing are commensurate with the risks identified. This approach should be an essential foundation to efficient allocation of resources across the anti-money laundering and countering the financing of terrorism (AML/CFT) regime and the implementation of risk- based measures throughout the FATF Recommendations. Where countries identify higher risks, they should ensure that their AML/CFT regime adequately addresses such risks. Where countries identify lower risks, they may decide to allow simplified measures for some of the FATF Recommendations under certain conditions. Countries should require financial institutions and designated non-financial businesses and professions (DNFBPs) to identify, assess and take effective action to mitigate their money laundering and terrorist financing risks.",
    section_id=sectionA.id)

recommendation2 = Recommendation(
    title="National cooperation and coordination",
    text="Countries should have national AML/CFT policies, informed by the risks identified, which should be regularly reviewed, and should designate an authority or have a coordination or other mechanism that is responsible for such policies. Countries should ensure that policy-makers, the financial intelligence unit (FIU), law enforcement authorities, supervisors and other relevant competent authorities, at the policy- making and operational levels, have effective mechanisms in place which enable them to cooperate, and, where appropriate, coordinate and exchange information domestically with each other concerning the development and implementation of policies and activities to combat money laundering, terrorist financing and the financing of proliferation of weapons of mass destruction. This should include cooperation and coordination between relevant authorities to ensure the compatibility of AML/CFT requirements with Data Protection and Privacy rules and other similar provisions (e.g. data security/localisation).",
    section_id=sectionA.id)

recommendation3 = Recommendation(
    title="Money laundering offence",
    text="Countries should criminalise money laundering on the basis of the Vienna Convention and the Palermo Convention. Countries should apply the crime of money laundering to all serious offences, with a view to including the widest range of predicate offences.",
    section_id=sectionB.id)


db.session.add(recommendation1)

db.session.add(recommendation2)

db.session.add(recommendation3)


db.session.commit()
print(sectionA)
print(recommendation1.title)
print(recommendation1.section_id)
print(sectionA.recommendations[0])



# recommendation1 = Recommendation("Assessing risks and applying a risk-based approach", "Countries should identify, assess, and understand the money laundering and terrorist financing risks for the country, and should take action, including designating an authority or mechanism to coordinate actions to assess risks, and apply resources, aimed at ensuring the risks are mitigated effectively. Based on that assessment, countries should apply a risk-based approach (RBA) to ensure that measures to prevent or mitigate money laundering and terrorist financing are commensurate with the risks identified. This approach should be an essential foundation to efficient allocation of resources across the anti-money laundering and countering the financing of terrorism (AML/CFT) regime and the implementation of risk- based measures throughout the FATF Recommendations. Where countries identify higher risks, they should ensure that their AML/CFT regime adequately addresses such risks. Where countries identify lower risks, they may decide to allow simplified measures for some of the FATF Recommendations under certain conditions.\nCountries should require financial institutions and designated non-financial businesses and professions (DNFBPs) to identify, assess and take effective action to mitigate their money laundering and terrorist financing risks.")
#
# recommendation2 = Recommendation("National cooperation and coordination", "Countries should have national AML/CFT policies, informed by the risks identified, which should be regularly reviewed, and should designate an authority or have a coordination or other mechanism that is responsible for such policies.\nCountries should ensure that policy-makers, the financial intelligence unit (FIU), law enforcement authorities, supervisors and other relevant competent authorities, at the policy- making and operational levels, have effective mechanisms in place which enable them to cooperate, and, where appropriate, coordinate and exchange information domestically with each other concerning the development and implementation of policies and activities to combat money laundering, terrorist financing and the financing of proliferation of weapons of mass destruction. This should include cooperation and coordination between relevant authorities to ensure the compatibility of AML/CFT requirements with Data Protection and Privacy rules and other similar provisions (e.g. data security/localisation).")

# db.session.add(recommendation1)
# db.session.add(recommendation2)
# db.session.commit()

# print(recommendation1)
