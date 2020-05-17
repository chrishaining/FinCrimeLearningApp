from project import db
from project.models import Section, Recommendation, GlossaryTerm

# I'm not sure why, but for this app I had to use db.create_all(). See https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/#creating-and-dropping-tables
db.create_all()

Section.query.delete()
Recommendation.query.delete()
GlossaryTerm.query.delete()



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
    text="Countries should identify, assess, and understand the money laundering and terrorist financing risks for the country, and should take action, including designating an authority or mechanism to coordinate actions to assess risks, and apply resources, aimed at ensuring the risks are mitigated effectively. Based on that assessment, countries should apply a risk-based approach (RBA) to ensure that measures to prevent or mitigate money laundering and terrorist financing are commensurate with the risks identified. This approach should be an essential foundation to efficient allocation of resources across the anti-money laundering and countering the financing of terrorism (AML/CFT) regime and the implementation of risk- based measures throughout the FATF Recommendations. Where countries identify higher risks, they should ensure that their AML/CFT regime adequately addresses such risks. Where countries identify lower risks, they may decide to allow simplified measures for some of the FATF Recommendations under certain conditions. \n\n Countries should require financial institutions and designated non-financial businesses and professions (DNFBPs) to identify, assess and take effective action to mitigate their money laundering and terrorist financing risks.",
    section_id=sectionA.id)

recommendation2 = Recommendation(
    title="National cooperation and coordination",
    text="Countries should have national AML/CFT policies, informed by the risks identified, which should be regularly reviewed, and should designate an authority or have a coordination or other mechanism that is responsible for such policies. \n\n Countries should ensure that policy-makers, the financial intelligence unit (FIU), law enforcement authorities, supervisors and other relevant competent authorities, at the policy- making and operational levels, have effective mechanisms in place which enable them to cooperate, and, where appropriate, coordinate and exchange information domestically with each other concerning the development and implementation of policies and activities to combat money laundering, terrorist financing and the financing of proliferation of weapons of mass destruction. This should include cooperation and coordination between relevant authorities to ensure the compatibility of AML/CFT requirements with Data Protection and Privacy rules and other similar provisions (e.g. data security/localisation).",
    section_id=sectionA.id)

recommendation3 = Recommendation(
    title="Money laundering offence",
    text="Countries should criminalise money laundering on the basis of the Vienna Convention and the Palermo Convention. Countries should apply the crime of money laundering to all serious offences, with a view to including the widest range of predicate offences.",
    section_id=sectionB.id)


recommendation4 = Recommendation(
    title="Confiscation and provisional measures",
    text="Countries should adopt measures similar to those set forth in the Vienna Convention, the Palermo Convention, and the Terrorist Financing Convention, including legislative measures, to enable their competent authorities to freeze or seize and confiscate the following, without prejudicing the rights of bona fide third parties: (a) property laundered, (b) proceeds from, or instrumentalities used in or intended for use in money laundering or predicate offences, (c) property that is the proceeds of, or used in, or intended or allocated for use in, the financing of terrorism, terrorist acts or terrorist organisations, or (d) property of corresponding value. \n\n Such measures should include the authority to: (a) identify, trace and evaluate property that is subject to confiscation; (b) carry out provisional measures, such as freezing and seizing, to prevent any dealing, transfer or disposal of such property; (c) take steps that will prevent or void actions that prejudice the country’s ability to freeze or seize or recover property that is subject to confiscation; and (d) take any appropriate investigative measures. \n\n Countries should consider adopting measures that allow such proceeds or instrumentalities to be confiscated without requiring a criminal conviction (non-conviction based confiscation), or which require an offender to demonstrate the lawful origin of the property alleged to be liable to confiscation, to the extent that such a requirement is consistent with the principles of their domestic law.",
    section_id=sectionB.id)

# recommendation3 = Recommendation(
#     title="",
#     text="",
#     section_id=)


db.session.add(recommendation1)

db.session.add(recommendation2)

db.session.add(recommendation3)

db.session.add(recommendation4)


glossaryTerm1 = GlossaryTerm(
    name="NCA",
    description="National Crime Agency")

db.session.add(glossaryTerm1)



db.session.commit()
# print(sectionA)
# print(recommendation1.title)
# print(recommendation1.section_id)
# print(sectionA.recommendations[0])
