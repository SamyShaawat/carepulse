# CarePulse - Odoo Practice Tasks for Clinics & Hospitals

*"Clinic operations, from patient to payment."*

These are practice tasks for building a clinic/hospital management module in Odoo. I wrote every task the way a real client would ask for it, so don't expect a click-by-click tutorial. Figuring out what the client actually needs is part of the work.

Build it, test it, and if you're making a portfolio video, record it.

## Before you start

- Create a custom module called `carepulse` and put all your work inside it.
- Even when a task is mostly setup (tags, stages, pricelists), try to save that setup in your module as XML or CSV data files. My test is simple: I install your module on a new, empty database and your work should be there. Anything you only clicked in the UI is gone with the database.
- Each task has an **Apps** line. Install those apps before you start the task.
- If you don't see an app called **Accounting**, use **Invoicing**. It covers everything these tasks need.
- Menu names and settings move around a bit between Odoo versions. If a hint points to something you can't find in your version, look for the same feature under a different name.
- Create some test data before testing: a few patients, 2 or 3 doctors and nurses (employees), some medicines, and 2 insurance companies.

## How to read each task

- **Scenario** - the problem, the way the client explains it to you. Read it like the client is sitting in front of you.
- **What to build** - what I expect you to deliver.
- **Done when** - the checklist I'll use to test your work. If every point works, the task is done.
- **Hints** - where to look in Odoo. Only read them if you're stuck.
- **Goal** - what the client gets out of it. If your solution works but doesn't reach the goal, it's not finished.
- **Depends on** - finish that task first, because this one builds on it.

If something is not clear, make a reasonable decision, write it down in a short note, and keep going. That's what you'd do with a real client too.

## Difficulty

- 🟢 **Easy** - one app, mostly configuration. Good for warming up.
- 🟡 **Medium** - one or two apps, with some automation or custom logic. Most real client work looks like this.
- 🔴 **Hard** - three or more apps, real business logic, and reporting across branches.

## Suggested order

M1 → M2 → M4 → M5 → M7 → M3 → M6 → M9 → M8 → M10 → M11

---

### 🟢 M1. Patient Records
**Apps:** Contacts, CRM

**Scenario:** A small clinic keeps patient info on paper cards. The receptionist wants to find any patient by name or phone, with allergies and blood type visible at a glance.

**What to build:**
1. New fields on the contact form:
   - **Allergies**
   - **Blood type** (a fixed list: A+, A-, B+, B-, AB+, AB-, O+, O-)
   - **Emergency contact** (name and phone)
2. Tags for patient type: **Child**, **Adult**, **Elderly**.
3. A list view that shows only patients, not suppliers, insurance companies, or other contacts.

**Done when:**
- The new fields are on the contact form and easy to spot.
- The patient list shows only patients, with blood type and allergies as columns.
- Searching by name or phone number finds the patient.
- The receptionist can filter the list by Child, Adult, or Elderly.

**Hints:**
- You need a way to tell which contacts are patients (a checkbox, a tag...). Your call.
- **New skill:** adding custom fields to an existing model and building saved filters.

**Goal:** A receptionist can find any patient's medical basics in under 5 seconds.

---

### 🟢 M2. Appointment Reminders
**Apps:** Calendar, CRM

**Scenario:** Patients keep forgetting their appointments, and the clinic loses money on no-shows.

**What to build:**
1. Three appointment types, each with its own duration: **Checkup**, **Follow-up**, **Emergency**. Pick sensible durations (for example 30, 20, and 60 minutes) and write them down.
2. An automatic email reminder sent to the patient **24 hours before** the appointment.

**Done when:**
- Picking an appointment type sets the right duration automatically.
- A patient with an appointment tomorrow gets a reminder email about 24 hours before.
- The email has the date, time, and type of the appointment.
- Staff do nothing by hand for the reminder to go out.

**Hints:**
- To test without waiting a day, create an appointment for tomorrow and run the scheduled action by hand (Settings > Technical > Scheduled Actions, needs developer mode).
- **New skill:** scheduled automated actions tied to a calendar event.

**Goal:** Fewer no-shows, because every patient gets a reminder automatically and staff do nothing.

---

### 🟡 M3. Online Doctor Booking
**Apps:** Calendar, Website
**Depends on:** M2

**Scenario:** The clinic wants patients to book their own appointments online instead of calling, but only during each doctor's real working hours.

**What to build:**
1. Working hours for each doctor.
2. Lunch breaks and days off blocked out.
3. An online booking page connected to all of this, which shows only slots that are really free.

**Done when:**
- A visitor who is not logged in can open the booking page, pick a doctor, and book a slot.
- Slots outside the doctor's working hours don't show.
- Lunch breaks and days off don't show.
- Once a slot is booked, nobody else can book it.
- The booking shows up in the doctor's calendar.

**Hints:**
- Search the Apps list for "appointment" to see if your Odoo has an online booking app. If it doesn't, build a simple booking page on the website that reads the doctor's working hours and existing appointments.

**Goal:** A patient books online, and the slot they pick is guaranteed to be free. No double bookings, no phone calls.

---

### 🟡 M4. Lab Test Billing with Insurance Discount
**Apps:** Sales, Accounting

**Scenario:** Some patients pay full price for lab tests. Others have insurance that covers 50% or 80%. The clinic wants this handled automatically, not with manual math every time.

**What to build:**
1. Lab tests as products, each with a base price.
2. A pricelist for each insurance provider that applies the right discount automatically.
3. Each patient is linked to their insurance, so the right pricelist is picked when that patient is selected.

**Done when:**
- A patient with no insurance pays the full price.
- A patient with 50% insurance gets 50% off, with no manual changes.
- A patient with 80% insurance gets 80% off.
- The discounted price is what shows on the invoice.

**Hints:**
- A contact can have a default pricelist (look at the Sales & Purchase tab).
- **New skill:** pricelists based on customer group.

**Goal:** Front desk selects the patient, and the correct discounted price shows up on the invoice with no calculation.

---

### 🟡 M5. Medicine Stock with Expiry Alerts
**Apps:** Inventory (plus Purchase)

**Scenario:** The hospital pharmacy has lost money on medicine that expired on the shelf without anyone noticing. Sometimes it also runs out of common medicine without warning.

**What to build:**
1. Track medicine by lot number, with an expiry date on each lot.
2. A minimum stock rule for each medicine, so the system creates a purchase request automatically when stock gets low.
3. A report of medicine that expires within the next 30 days.

**Done when:**
- Receiving medicine asks for a lot number and an expiry date.
- When stock drops below the minimum, a purchase request (RFQ) is created without anyone asking for it.
- The expiry report lists only lots expiring in the next 30 days, with the medicine, the lot, the quantity, and the date.

**Hints:**
- Turn on **Lots & Serial Numbers** and **Expiration Dates** in Inventory settings.
- Stock rules create purchase requests only if Purchase is installed.
- **New skill:** lot/expiry tracking and reordering rules.

**Goal:** The pharmacist is warned before medicine expires and before it runs out, instead of finding out too late.

---

### 🟡 M6. Nurse Shift Scheduling
**Apps:** Employees, Attendances

**Scenario:** The head nurse writes the shift schedule on a whiteboard by hand, and it becomes a mess when someone calls in sick.

**What to build:**
1. Working schedules for **morning** and **night** shifts, assigned to each nurse.
2. Kiosk check-in and check-out for nurses.
3. A report that shows who is on shift right now.

**Done when:**
- Each nurse has a morning or night schedule.
- A nurse checks in at the kiosk and shows up in the "on duty now" report.
- When they check out, they drop off the report.
- The head nurse can open the report at any time and trust it.

**Hints:**
- Think about night shifts that start one day and end the next.

**Goal:** The head nurse can see at any moment exactly who is on duty.

---

### 🟡 M7. Patient Follow-up Pipeline
**Apps:** CRM
**Depends on:** M1

**Scenario:** After a diagnosis, patients need follow-up calls (test results, checking their medicine, checking their recovery), but the clinic keeps forgetting to call some of them.

**What to build:**
1. A CRM pipeline with these stages: **Consultation → Diagnosis → Treatment → Recovery Check**.
2. When a patient moves to **Recovery Check**, an activity (a reminder to call) is created automatically for the patient's doctor.

**Done when:**
- The pipeline shows the 4 stages in the right order.
- Moving a patient to Recovery Check creates one activity, assigned to that patient's doctor.
- The doctor sees it in their activities list.
- Moving the patient to another stage doesn't create the activity.

**Hints:**
- Decide which field on the lead represents "the doctor". The salesperson field is the obvious one.
- Look at automated actions (called automation rules in newer versions).

**Goal:** No patient is forgotten. The system reminds the doctor to make the follow-up call.

---

### 🟡 M8. Full Cycle - Clinic Visit to Paid Invoice
**Apps:** CRM, Sales, Inventory, Accounting
**Depends on:** M1, M4, M5

**Scenario:** Right now a patient's visit, their medicine, and their payment are tracked in three different notebooks, and it's hard to know if a bill was actually paid.

**What to build:** Connect these steps so each one comes from the one before it:
1. The patient visit is logged as a CRM opportunity.
2. The consultation is quoted as a sale order.
3. The medicine given to the patient is taken out of pharmacy stock automatically.
4. The invoice is created from the sale order.
5. The payment is recorded and reconciled.

**Done when:**
- You can run one patient visit from arrival to paid invoice without typing the same data twice.
- Pharmacy stock goes down by the right quantity, from the right lot.
- The insurance discount from M4 is applied when the patient has insurance.
- From the opportunity you can open the sale order, the delivery, the invoice, and the payment.
- The invoice shows as **Paid**.

**Hints:**
- Most of these links already exist in Odoo. Your job is to make sure nothing breaks between the steps and to fill any gaps.
- This is a great one to record. Show one patient going through the whole flow.

**Goal:** One patient visit, one continuous digital trail from arrival to paid invoice, with pharmacy stock updating on its own.

---

### 🟡 M9. Insurance Company Debt Tracking
**Apps:** Accounting

**Scenario:** Insurance companies owe the hospital money for treatments already given, and finance has no clear view of how much each one owes or how overdue it is.

**What to build:**
1. Set up each insurance company as its own account (vendor/customer).
2. Track partial payments against invoices.
3. An aging report showing how much is overdue and for how long.

**Done when:**
- A 10,000 invoice with a 4,000 payment shows 6,000 still owed.
- The aging report shows each insurance company on its own line.
- Overdue amounts are split by age (for example 1-30, 31-60, 61-90, 90+ days).
- The finance manager can open the invoices behind any number.

**Hints:**
- Check whether your Odoo already has an aged receivable report before building your own. If it doesn't, a pivot or list view of unpaid invoices grouped by insurance company and by how many days overdue does the job.

**Goal:** The finance manager opens one report and knows right away which insurance company owes what, and since when.

---

### 🔴 M10. Multi-Branch Hospital Dashboard
**Apps:** Accounting, Employees, Inventory

**Scenario:** A hospital group has 3 branches. Management wants one dashboard comparing revenue, doctor performance, and medicine stock across all branches, instead of three separate spreadsheets.

**What to build:**
1. Set up each branch as a separate company or analytic account. Explain which one you picked and why.
2. A financial report by branch.
3. A doctor performance KPI: patients seen and revenue brought in per doctor.
4. A stock view comparing medicine levels across branches.

**Done when:**
- Management opens one screen and sees all 3 branches next to each other: money, people, and stock.
- They can filter by period.
- The numbers match the real invoices, visits, and stock.

**Hints:**
- Pivot and graph views go a long way. If they're not enough, look at dashboards/spreadsheets or a custom report model.

**Goal:** Management opens one screen and sees all 3 branches side by side: money, people, and stock.

---
### 🔴 M11. Visit Notes and Printed Prescription
**Apps:** Contacts, Calendar, Inventory
**Depends on:** M1, M5

**Why this task:** Every clinic needs a medical record: what the patient came for, what the doctor found, what was prescribed. It's the first thing any doctor asks for, and Odoo has no medical record of any kind.

**Scenario:** After each consultation the doctor writes notes on paper and hands the patient a handwritten prescription. Next visit, nobody can find the old notes. Pharmacists struggle to read the handwriting. Once, a patient was prescribed a medicine they were allergic to because the allergy was written on a different card.

**What to build:**
1. A **visit record** for every consultation, linked to the patient and the appointment, with:
   - Complaint (why they came)
   - Examination notes
   - Diagnosis
   - Doctor
2. **Prescription lines** on the visit: medicine (from the pharmacy's products), dose, how often, how many days.
3. A **warning** when the doctor prescribes something that matches one of the patient's allergies from M1.
4. A **printed prescription** (PDF) with the clinic's header, patient, date, doctor, and the medicines in clear print.
5. A **patient history**: all past visits for a patient, newest first, visible from the patient's form.

**Done when:**
- A doctor can open today's appointment, write the visit notes, and add prescription lines without leaving that screen.
- Prescribing a medicine the patient is allergic to shows a clear warning before saving.
- The prescription prints as a clean one-page PDF that a pharmacist can read.
- Opening a patient shows every past visit with its diagnosis and prescription.
- Only doctors can see and edit the visit notes. The receptionist can see that a visit happened but not what's in it.

**Hints:**
- The allergy check can be simple to start with: match the medicine against the allergies written on the patient. Say in your note how you'd make it smarter.
- Medical notes are private. Plan the access rights before you build the screens.

**Goal:** Every consultation is recorded, the patient's full history is one click away, prescriptions are readable, and the system catches allergies before the patient does.

---

## Best task for your portfolio video

Pick **M8 - Full Cycle: Clinic Visit to Paid Invoice**. It shows CRM, Sales, Inventory, and Accounting working together as one flow, which is exactly what clients hire an Odoo developer for.

## What to hand in

- Your `carepulse` module (it should install on a new database without errors).
- A short note with any decisions you made where the task left the choice to you.
- Optional: a short video of the task working.
