import pandas as pd
import streamlit as st
import plotly.express as px
import io

# ----------------- 페이지 설정 -----------------
st.set_page_config(page_title="인정평가 부적합 분석(ISO/IEC 17021-1 기반)", layout="wide")

# ----------------- 상단 로고 + 제목 -----------------
st.markdown(
    """
    <div style="display:flex; align-items:center;">
        <img src="https://img.icons8.com/color/96/000000/book.png" width="60" style="margin-right:15px"/>
        <h1 style="margin:0;"> 부적합 작성 가이드</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------- 가이드 탭 -----------------
tab1, tab2, tab3 = st.tabs(["📖 부적합 정의", "✍️ 부적합 작성법", "⚖️ 부적합 vs 권고사항"])

with tab1:
    st.markdown("""
### 부적합 (Nonconformity)이란
**ISO 정의**  
> *non-fulfillment of a requirement*  
즉, 어떤 요구사항(requirement) 을 충족하지 못한 상태를 의미합니다.  

ISO 9001 심사 실행 지침 등 ISO Auditing Practices Group 문서에서도 이 정의를 사용하며, 부적합을 문서화할 때는 **“요구사항 위반 → 객관적 증거 → 원인 → 시정 조치 → 재발 방지 계획”** 체계가 필요합니다.  

인증심사 가이드라인인 ISO 19011:2018에서는 “audit findings (심사 결과)” 개념을 다루며, 심사 결과는 기준(criterion) 대비 현실(실제 상태)을 평가한 결과로서, conformity 또는 nonconformity 가 될 수 있다고 규정합니다. 따라서 ISO 체계에서 부적합은 “심사기준(표준, 규정, 내부 문서 등) 중 하나 이상의 요구사항을 충족하지 못한 상태”로 간주됩니다.
""")

with tab2:
    st.markdown("""
### 부적합 작성법
아래는 ISO 9001 Auditing Practices Group(APG) 문서와 ISO/ISO 19011, ISO 17021-1 등에 기반한 부적합 작성 가이드입니다.

**주요 원칙 및 구성요소** APG 문서는 “a well-documented nonconformity”를 위해 다음 세 부분이 반드시 포함되어야 한다고 안내합니다: 심사 증거 (audit evidence) 요구사항 (requirement) 부적합 진술 (statement of nonconformity)

| 항목 | 설명 | 출처 |
|------|------|------|
| **심사 증거** | 객관적 사실·기록 등 구체적 증거 명시 | ISO/APG |
| **요구사항** | 위반한 기준 조항을 명확히 표기 | ISO 17021-1 |
| **부적합 진술** | 위반 내용을 간결·명확하게 기술 | ISO/APG |
| **시정·원인분석·재발방지** | 시정(Correction), 시정조치(CA), 재발방지 포함 | ISO/APG |
| **검증 및 종결** | 평가사(심사원)이 조치 유효성 검증 후 종결 | ISO/APG |
""")

with tab3:
    st.markdown("""
### 부적합 (Nonconformity) vs 권고사항 / 개선기회 (Recommendation / OFI)의 구별 — "기준과 실제 구분"
부적합과 권고사항(또는 “개선 기회, Observation / OFI”)은 평가 및 관리 시스템 운영 시 자주 혼동되는 개념이므로, 구별 기준을 명확히 두는 것이 중요합니다. 아래 기준들을 중심으로 설명드립니다. 

(1) ISO 관점: 권고사항/개선기회는 정의된 용어가 아님 ISO 9000 / ISO 19011 / ISO 17021 등의 표준에는 “Opportunity for Improvement / Recommendation” 이라는 용어의 공식 정의는 없습니다. 

심사 지침에서는 심사원이 부적합을 지적으로 할 수 없는 경우라도 시스템 개선 가능성 등에 대해 의견을 제시할 수 있음을 인정하지만, 권고사항은 의무 조치 항목은 아니다 라는 점이 강조됩니다. 

ISO/IEC 17021-1:2015 (인증기관에 대한 요구사항)에서는 관찰(observation) 또는 개선 기회가 식별되고 기록될 수 있으나, 평가 결과가 nonconformity인 경우에는 그것을 개선 기회로 기록해서는 안 된다고 정의하고 있으며, 개선 기회는 표준 위반의 증거가 없는 영역에서 제시 가능한 조언 수준으로 다루어 지고 있습니다. 

ISO 19011:2018 제6.4.10항에서는 “recommendations (권고사항)” 또는 “opportunities for improvement”는 심사 목적에 따라 제시될 수 있지만, 이는 성능 개선을 위한 의견이지 필수 준수 대상은 아니라고 명시합니다. 

즉, ISO 체계에서는 권고사항 또는 개선기회는 평가사(심사원)이 제안할 수 있는 개선 아이디어 수준이며, 부적합과는 별도로 취급됩니다. 


(2) 실무적/판단 기준으로의 구별 요소*** 

아래 요소들을 기준으로 “이건 부적합인가, 개선 기회인가”를 구별하는 것이 일반적입니다.

| 구별 기준 | 부적합 (Nonconformity) | 권고사항 / 개선기회 (OFI, Recommendation) | | -------------------- | ---------------------------------- | --------------------------------------- | | **요구사항 위반 여부** | 기준 또는 요구사항을 명백히 위반한 경우 | 요구사항을 위반하지 않았지만 더 나은 방법이 있을 경우 | | **의무 조치 여부** | 반드시 시정 조치가 요구됨 | 조치가 의무는 아니며 조직의 선택 사항 | | **인증 또는 적합성 영향 가능성** | 인증 유지, 시스템 신뢰성 등에 영향을 줄 수 있음 | 일반적으로 인증 불이행으로 직접 연결되지는 않음 | | **심각성 / 위험도** | 시스템 취약, 반복 발생, 안전/품질 영향 등 | 주로 효율성, 최적화, 비용 절감 등 개선 여지 | | **명령적 표현 사용 여부** | “~하지 않음”, “~이 없음”, “~미준수” 등 부정적 표현 | “~필요함”, “권장됨”, “검토할 필요 있음” 등 제안형 표현 | """))

st.markdown("---")

# ----------------- 기본 데이터 -----------------
DEFAULT_FINDINGS = pd.DataFrame({
    "인정기준": ["KAB-R-MSCB"]*6,
    "조항": ["7", "7.1", "7.2", "8.3", "9.1", "9.2"],
    "세부조항": ["7.1", "7.1.1", "7.1.2", "8.3.1", "9.1.1", "9.2.2"],
    "구분": ["부적합", "권고", "부적합", "권고", "부적합", "권고"],
    "내용": [
        "조직은 품질경영시스템 자원의 충분성을 확보하지 못함.",
        "프로세스 운영계획서에 인원 배치가 미흡함.",
        "고객 요구사항 검토 절차 미이행.",
        "변경관리 절차서가 최신화되어 있지 않음.",
        "내부심사 계획이 적시에 수립되지 않음.",
        "고객만족도 조사 절차 개선 필요."
    ]
})
DEFAULT_STANDARDS = pd.DataFrame({
    "조항": ["7", "7.1", "7.2", "8.3", "9.1", "9.2"],
    "요구사항": [
        "조직은 필요한 자원을 결정하고 제공해야 한다.",
        "조직은 인프라를 포함한 필요한 자원을 제공해야 한다.",
        "조직은 인적 자원의 역량을 보장해야 한다.",
        "제품 및 서비스 설계개발을 관리해야 한다.",
        "모니터링 및 측정을 통해 시스템 성과를 평가해야 한다.",
        "내부심사를 계획하고 실시해야 한다."
    ]
})

# ----------------- 유틸 -----------------
def drop_noise_columns(df):
    noise = {"기관명","평가종류","시작일","종료일","발행번호"}
    unnamed = [c for c in df.columns if str(c).startswith("Unnamed")]
    return df.drop(columns=list(noise)+unnamed, errors="ignore")

def add_req_text(findings, standards):
    if standards is None: return findings
    std_cols = standards.columns
    clause_col = next((c for c in std_cols if c in ["조항","Clause","항목"]), None)
    req_col = next((c for c in std_cols if c in ["요구사항","Requirement","내용"]), None)
    if not clause_col or not req_col: return findings
    std = standards.copy()
    std[clause_col] = std[clause_col].astype(str)
    f = findings.copy()
    def match_req(row):
        sub = str(row.get("세부조항")); main = str(row.get("조항"))
        if sub in std[clause_col].values: return std.loc[std[clause_col]==sub, req_col].values[0]
        if main in std[clause_col].values: return std.loc[std[clause_col]==main, req_col].values[0]
        return ""
    f["요구사항"] = f.apply(match_req, axis=1)
    return f

# ----------------- 데이터 로드 -----------------
uploaded = st.file_uploader("엑셀 파일 업로드 (선택)", type=["xlsx"])
if uploaded:
    findings = pd.read_excel(uploaded, sheet_name=0)
    try: standards = pd.read_excel(uploaded, sheet_name=1)
    except: standards = DEFAULT_STANDARDS
else:
    st.info("⚠️ 업로드하지 않으면 샘플 데이터를 사용합니다.")
    findings, standards = DEFAULT_FINDINGS.copy(), DEFAULT_STANDARDS.copy()

findings = drop_noise_columns(findings)
findings = add_req_text(findings, standards)

# ----------------- 검색 조건 -----------------
st.sidebar.header("🔍 검색 조건")
조항_sel = st.sidebar.multiselect("조항", sorted(findings["조항"].dropna().astype(str).unique()) if "조항" in findings else [])
세부조항_sel = st.sidebar.multiselect("세부조항", sorted(findings["세부조항"].dropna().astype(str).unique()) if "세부조항" in findings else [])
구분_sel = st.sidebar.multiselect("구분 (부적합/권고)", sorted(findings["구분"].dropna().astype(str).unique()) if "구분" in findings else [])
키워드 = st.sidebar.text_input("내용 검색")
조항검색 = st.sidebar.text_input("조항 검색 (예: 7 또는 7.1)")
if st.sidebar.button("검색조건 초기화"):
    st.experimental_rerun()
btn_search = st.sidebar.button("🔍 검색 실행")

# ----------------- 필터링 -----------------
df = findings.copy()
if btn_search or any([조항_sel, 세부조항_sel, 구분_sel, 키워드, 조항검색]):
    if "조항" in df and 조항_sel: df = df[df["조항"].astype(str).isin(조항_sel)]
    if "세부조항" in df and 세부조항_sel: df = df[df["세부조항"].astype(str).isin(세부조항_sel)]
    if "구분" in df and 구분_sel: df = df[df["구분"].astype(str).isin(구분_sel)]
    if "내용" in df and 키워드: df = df[df["내용"].astype(str).str.contains(키워드, case=False, na=False)]
    if 조항검색:
        mask = pd.Series(False, index=df.index)
        if "조항" in df: mask |= df["조항"].astype(str).str.contains(조항검색, na=False)
        if "세부조항" in df: mask |= df["세부조항"].astype(str).str.contains(조항검색, na=False)
        df = df[mask]

st.markdown("### 🔎 검색 결과")
st.dataframe(df[[c for c in ["조항","세부조항","구분","요구사항","내용"] if c in df.columns]], use_container_width=True, hide_index=True)

# ----------------- 통계 -----------------
st.markdown("## 📊 통계 분석")
if not df.empty:
    if "조항" in df:
        st.markdown("#### 1️⃣ 조항별 발생 건수")
        c1 = df["조항"].astype(str).value_counts().reset_index()
        c1.columns=["조항","건수"]
        st.plotly_chart(px.bar(c1, x="조항", y="건수", text="건수", title="조항별 발생 건수"), use_container_width=True)
    if "세부조항" in df:
        st.markdown("#### 2️⃣ 세부조항별 발생 건수")
        c2 = df["세부조항"].astype(str).value_counts().reset_index()
        c2.columns=["세부조항","건수"]
        fig2 = px.bar(c2, x="세부조항", y="건수", text="건수", title="세부조항별 발생 건수")
        fig2.update_xaxes(tickangle=60)
        st.plotly_chart(fig2, use_container_width=True)
    if "구분" in df:
        st.markdown("#### 3️⃣ 권고 / 부적합 비율")
        st.plotly_chart(px.pie(df, names="구분", title="권고/부적합 비율"), use_container_width=True)
